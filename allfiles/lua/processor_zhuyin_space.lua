--- @@ zhuyin_space
--[[
注音反查 Return 和 space 和 小鍵盤數字鍵 上屏修正
尚有bug待處理
--]]


-- local function status(ctx)
--     local stat = metatable()
--     local comp = ctx.composition
--     stat.always = true
--     stat.composing = ctx:is_composing()
--     stat.empty = not stat.composing
--     stat.has_menu = ctx:has_menu()
--     stat.paging = not comp:empty() and comp:back():has_tag("paging")
--     return stat
-- end


----------------------------------------------------------------------------------------
local utf8_sub = require("f_components/f_utf8_sub")
----------------------------------------------------------------------------------------


-- local function zhuyin_space(key,env)
local function processor(key, env)
  local engine = env.engine
  local context = engine.context
  local comp = context.composition
  local seg = comp:back()
  -- local page_size = engine.schema.page_size
  local o_ascii_mode = context:get_option("ascii_mode")
  local c_input = context.input
  -- local g_s_t = context:get_script_text()
  local g_c_t = context:get_commit_text()
  local key_num = key:repr():match("KP_([0-9])") or key:repr():match("Control%+([0-9])")

  local set_char_bpmf = Set {"ㄅ", "ㄆ", "ㄇ", "ㄈ", "ㄉ", "ㄊ", "ㄋ", "ㄌ", "ㄍ", "ㄎ", "ㄏ", "ㄐ", "ㄑ", "ㄒ", "ㄓ", "ㄔ", "ㄕ", "ㄖ", "ㄗ", "ㄘ", "ㄙ", "ㄧ", "ㄨ", "ㄩ", "ㄚ", "ㄛ", "ㄜ", "ㄝ", "ㄞ", "ㄟ", "ㄠ", "ㄡ", "ㄢ", "ㄣ", "ㄤ", "ㄥ", "ㄦ", "ˉ", "ˊ", "ˇ", "ˋ", "˙", "ㄪ", "ㄫ", "ㄫ", "ㄬ", "ㄭ", "ㄮ", "ㄮ", "ㄯ", "ㄯ", "ㆠ", "ㆡ", "ㆢ", "ㆣ", "ㆤ", "ㆥ", "ㆦ", "ㆧ", "ㆨ", "ㆩ", "ㆪ", "ㆫ", "ㆬ", "ㆭ", "ㆭ", "ㆮ", "ㆯ", "ㆰ", "ㆰ", "ㆱ", "ㆱ", "ㆲ", "ㆲ", "ㆳ", "ㆴ", "ㆵ", "ㆶ", "ㆷ", "ㆸ", "ㆹ", "ㆺ"}

  -- local s = status(context)
  --- 不要使用以下作為選擇項和未選擇項計算，太困難了，因 preedit 除注音字節，還包含不確定的分節空白。
  -- local start = context:get_preedit().sel_start
  -- local _end = context:get_preedit().sel_end
  -- local es = _end - start
  -- local caret_pos = context.caret_pos


-----------------------------------------------------------------------------

  if o_ascii_mode then
    return 2

  --- prevent segmentation fault (core dumped) （避免進入死循環，有用到 seg=comp:back() 建議使用去排除？）
  elseif comp:empty() then
    return 2

  elseif not seg:has_tag("reverse2_lookup") and not seg:has_tag("all_bpm") then
    return 2

  elseif not context:has_menu() then
  -- elseif not context:is_composing() then  --無法空碼清屏
    return 2

  --- pass release alt super (not pass ctrl)
  elseif key:release() or key:alt() or key:super() then
    return 2

  --- pass not space Return KP_Enter key_num
  elseif key:repr() ~= "space" and key:repr() ~= "Return" and key:repr() ~= "KP_Enter" and not key_num then
    return 2

---------------------------------------------------------------------------
--[[
以下針對反查注音 Bug 作修正
--]]

  --- 以下修正：附加方案鍵盤範圍大於主方案時，選字時出現的 bug。
  elseif seg:has_tag("paging") and ( key:repr() == "space" or key:repr() == "Return" or key:repr() == "KP_Enter" ) then

    --- 先上屏 paging 時選擇的選項
    -- local selected_candidate_index = seg.selected_index
    -- context:select(selected_candidate_index)
    local cand = context:get_selected_candidate()
    engine:commit_text(cand.text)
    -- engine:commit_text(cand.text..start.." ".._end.." "..#c_input.." "..caret_pos )  --測試各個位置數值用

    --- 計算末尾殘留的非中文字元數（未被選擇的 cand.input 字元數）
    local n_gct_cut = #string.gsub(g_c_t, "[^.,;/ %w-]", "")  -- 刪除中文編碼後，計算字數。
    -- context:confirm_current_selection()
    -- context:refresh_non_confirmed_composition()

    --- 補前綴 "';" 或 "';'"，導入未上屏編碼，避免跳回主方案
    if n_gct_cut == 0 then
      context:clear()
    elseif seg:has_tag("reverse2_lookup") then
      context.input = "';" .. string.sub(c_input, -n_gct_cut)
    elseif seg:has_tag("all_bpm") then
      context.input = "';'" .. string.sub(c_input, -n_gct_cut)
    end
    return 1


  --- 以下修正：附加方案鍵盤範圍大於主方案時，小板數字鍵選擇出現之 bug。
  elseif key_num then
    --- 確定選項編號
    -- 以下針對選字編碼為：012345678
    local page_n = 9 * (seg.selected_index // 9)    -- 先確定在第幾頁
    local key_num2 = tonumber(key_num)
    if key_num2 == 9 then    -- 方案預設沒有選項9，故跳掉。
      return 1
    elseif key_num2 > 0 then
      key_num2 = key_num2 + page_n
    elseif key_num2 == 0 then
      key_num2 = key_num2 + page_n
    end

    --- 上屏選擇選項。
    local cand = seg:get_candidate_at(key_num2)
    engine:commit_text(cand.text)

    --- 判別掛載方案，依不同方案分別處理：
    --- 刪除已上屏字詞的前頭字元。
    if seg:has_tag("reverse2_lookup") then
      local cand_len = utf8.len(cand.text)
      local ci_cut = string.gsub(c_input, "^';", "")
      -- 上屏詞彙為單個注音
      if set_char_bpmf[cand.text] then
        ci_cut = string.gsub(ci_cut, "^[.,;/ %w-]", "")
      -- 上屏詞彙為兩個注音
      elseif (cand_len == 2) and set_char_bpmf[utf8_sub(cand.text, 1, 1)] and set_char_bpmf[utf8_sub(cand.text, 2, 2)] then
        ci_cut = string.gsub(ci_cut, "^[.,;/ %w-][.,;/ %w-]", "")
      -- 上屏詞彙為三個注音
      elseif (cand_len == 3) and set_char_bpmf[utf8_sub(cand.text, 1, 1)] and set_char_bpmf[utf8_sub(cand.text, 2, 2)] and set_char_bpmf[utf8_sub(cand.text, 3, 3)] then
        ci_cut = string.gsub(ci_cut, "^[.,;/ %w-][.,;/ %w-][.,;/ %w-]", "")
      -- 上屏詞彙為全中文不含注音，但有狀況會缺漏出現 bug
      else
        for i = 1, cand_len do
          ci_cut = string.gsub(ci_cut, "^[.,;/a-z125890-][.,;/a-z125890-]?[.,;/a-z125890-]?[ 3467]", "")
        end
      end
      --- 補前綴 "';"，導入未上屏編碼，避免跳回主方案
      if #ci_cut == 0 then
        context:clear()
      else
        context.input = "';" .. ci_cut
      end

    elseif seg:has_tag("all_bpm") then
      local cand_len = utf8.len(cand.text)
      local ci_cut = string.gsub(c_input, "^';'", "")
      for i = 1, cand_len do
        ci_cut = string.gsub(ci_cut, "^[.,;/ %w-]", "")
      end
      --- 補前綴 "';'"，導入未上屏編碼，避免跳回主方案
      if #ci_cut == 0 then
        context:clear()
      else
        context.input = "';'" .. ci_cut
      end
    end

    return 1

---------------------------------------------------------------------------

  --- 某些方案輸入 Return 出英文，該條限定注音 Return 一律直上中文。
  elseif key:repr() == "Return" or key:repr() == "KP_Enter" then
    engine:commit_text(g_c_t)
    context:clear()
    return 1

  --- 如果末尾為聲調則跳掉，按空白鍵，則 Rime 上屏，非 lua 作用。
  elseif string.match(c_input, "[ 3467]$") then
    return 2

  --- 補掛接反查注音不能使用空白當作一聲
  elseif key:repr() == "space" then
  -- elseif key:repr() == "space" then
  -- elseif key:repr() == "space" and context:has_menu() then
    -- engine:commit_text(c_input .. "_")
    context.input = c_input .. " "
    -- context:clear()
    return 1

  end

  return 2
end


-- return zhuyin_space
return { func = processor }