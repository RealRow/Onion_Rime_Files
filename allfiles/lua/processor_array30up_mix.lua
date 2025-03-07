--- @@ 合併 array30up 和 array30up_zy
--[[
（onion-array30）
行列30三四碼字按空格直接上屏
行列30注音反查 Return 和 space 和 小鍵盤數字鍵 上屏修正
尚有bug待處理
--]]

----------------------------------------------------------------------------------------
local utf8_sub = require("f_components/f_utf8_sub")
----------------------------------------------------------------------------------------


-- local function array30up_mix(key, env)
local function processor(key, env)
  local engine = env.engine
  local context = engine.context
  local comp = context.composition
  local seg = comp:back()
  -- local page_size = engine.schema.page_size
  local o_ascii_mode = context:get_option("ascii_mode")
  local a_s_wp = context:get_option("array30_space_wp")
  local a_r_abc = context:get_option("array30_return_abc")
  local c_input = context.input
  -- local g_s_t = context:get_script_text()
  local g_c_t = context:get_commit_text()
  local key_num = key:repr():match("KP_([0-9])") or key:repr():match("Control%+([0-9])")

  local set_char_bpmf = Set {"ㄅ", "ㄆ", "ㄇ", "ㄈ", "ㄉ", "ㄊ", "ㄋ", "ㄌ", "ㄍ", "ㄎ", "ㄏ", "ㄐ", "ㄑ", "ㄒ", "ㄓ", "ㄔ", "ㄕ", "ㄖ", "ㄗ", "ㄘ", "ㄙ", "ㄧ", "ㄨ", "ㄩ", "ㄚ", "ㄛ", "ㄜ", "ㄝ", "ㄞ", "ㄟ", "ㄠ", "ㄡ", "ㄢ", "ㄣ", "ㄤ", "ㄥ", "ㄦ", "ˉ", "ˊ", "ˇ", "ˋ", "˙", "ㄪ", "ㄫ", "ㄫ", "ㄬ", "ㄭ", "ㄮ", "ㄮ", "ㄯ", "ㄯ", "ㆠ", "ㆡ", "ㆢ", "ㆣ", "ㆤ", "ㆥ", "ㆦ", "ㆧ", "ㆨ", "ㆩ", "ㆪ", "ㆫ", "ㆬ", "ㆭ", "ㆭ", "ㆮ", "ㆯ", "ㆰ", "ㆰ", "ㆱ", "ㆱ", "ㆲ", "ㆲ", "ㆳ", "ㆴ", "ㆵ", "ㆶ", "ㆷ", "ㆸ", "ㆹ", "ㆺ"}

  local check_i1 = string.match(c_input, "^[a-z.,/;][a-z.,/;][a-z.,/;][a-z.,/;]?i?$")
  local check_i2 = string.match(c_input, "^==[a-z.,/;][a-z.,/;][a-z.,/;][a-z.,/;]?i?$")
  local check_i3 = string.match(c_input, "`.+$")
  -- local check_i4 = string.match(c_input, "^[a-z][-_.0-9a-z]*@.*$")
  -- local check_i5 = string.match(c_input, "^https?:.*$")
  -- local check_i6 = string.match(c_input, "^ftp:.*$")
  -- local check_i7 = string.match(c_input, "^mailto:.*$")
  -- local check_i8 = string.match(c_input, "^file:.*$")
  local check_i4 = string.match(c_input, "^[a-z][-_.0-9a-z]*@.*$") or
                   string.match(c_input, "^https?:.*$") or
                   string.match(c_input, "^ftp:.*$") or
                   string.match(c_input, "^mailto:.*$") or
                   string.match(c_input, "^file:.*$")
  -- local check_zh = string.match(c_input, "^=[a-z0-9,.;/-]+$")
  -- local check_w = string.match(c_input, "^w[0-9]$")
  -- local check_abc = string.match(c_input, "^[a-z,./;]+$")


-----------------------------------------------------------------------------

  if o_ascii_mode then
    return 2

  --- prevent segmentation fault (core dumped) （避免進入死循環，有用到 seg=comp:back() 建議使用去排除？）
  elseif comp:empty() then
    return 2

  --- pass release alt super (not pass ctrl)
  elseif key:release() or key:alt() or key:super() then
    return 2

  --- pass not space Return KP_Enter key_num
  elseif key:repr() ~= "space" and key:repr() ~= "Return" and key:repr() ~= "KP_Enter" and not key_num then
    return 2

-----------------------------------------------------------------------------

  --- return 上屏候選字或英文，設開關（以下 abc 非英文，而是中文主 segmentor）

  elseif (a_r_abc) and (seg:has_tag("abc")) and (key:repr() == "Return" or key:repr() == "KP_Enter") then
  -- elseif a_r_abc and check_abc and key:repr() == "Return" or key:repr() == "KP_Enter" then

    -- --- 選字時 Return 上屏選項
    -- if not seg:has_tag("paging") then
    --   engine:commit_text(c_input)
    --   context:clear()
    --   return 1
    -- end

    --- 全狀態（開關符號以 space 翻頁時除外） Return 都上屏英文
    engine:commit_text(c_input)
    context:clear()
    return 1

-----------------------------------------------------------------------------

  elseif not context:has_menu() then
  -- elseif not context:is_composing() then  -- 無法空碼清屏
    return 2

  elseif check_i1 or check_i2 or check_i3 or check_i4 then
  -- elseif check_i1 or check_i2 or check_i3 or check_i4 or check_i5 or check_i6 or check_i7 or check_i8 then
    if key:repr() == "space" then
      -- local g_c_t = context:get_commit_text()
      engine:commit_text(g_c_t)
      context:clear()
      return 1 -- kAccepted
    else
      return 2
    end

-----------------------------------------------------------------------------
  --- 使 w[0-9] 輸入符號時：空白鍵同某些行列 30 一樣為翻頁。
  --- KeyEvent 函數在舊版 librime-lua 中不支持。
  --- 增設開關。

  -- elseif a_s_wp and seg:has_tag("wsymbols") then
  -- -- elseif a_s_wp and check_w then
  --   if key:repr() == "space" then
  --     engine:process_key(KeyEvent("Page_Down"))
  --     return 1 -- kAccepted
  --   --- 修正 w[0-9] 空白鍵 設翻頁時，無上屏鍵問題。
  --   --- 搭配前面「空白鍵同某些行列 30 一樣為翻頁」，並且用 custom 檔設「return 上屏候選字」，校正 Return 能上屏候選項！
  --   elseif key:repr() == "Return" or key:repr() == "KP_Enter" then
  --     engine:commit_text(g_c_t)
  --     context:clear()
  --     return 1 -- kAccepted
  --   end

  -- --- 修正 Return 都上屏英文時， w[0-9] 空白鍵為上屏鍵，Return 還是上屏候選項問題。
  -- elseif (a_r_abc) and (not a_s_wp) and (seg:has_tag("wsymbols")) and (key:repr() == "Return" or key:repr() == "KP_Enter") then
  --   engine:commit_text(c_input)
  --   context:clear()
  --   return 1

  elseif seg:has_tag("wsymbols") then
    if a_s_wp then
      if key:repr() == "space" then
        engine:process_key(KeyEvent("Page_Down"))
        return 1 -- kAccepted
      --- 修正 w[0-9] 空白鍵 設翻頁時，無上屏鍵問題。
      --- 搭配前面「空白鍵同某些行列 30 一樣為翻頁」，並且用 custom 檔設「return 上屏候選字」，校正 Return 能上屏候選項！
      elseif key:repr() == "Return" or key:repr() == "KP_Enter" then
        engine:commit_text(g_c_t)
        context:clear()
        return 1 -- kAccepted
      end
    --- 修正 Return 都上屏英文時， w[0-9] 空白鍵為上屏鍵，Return 還是上屏候選項問題。
    elseif a_r_abc then
    -- elseif not a_s_wp and a_r_abc then
      if key:repr() == "Return" or key:repr() == "KP_Enter" then
        engine:commit_text(c_input)
        context:clear()
        return 1
      end
    end

---------------------------------------------------------------------------
--[[
以下針對反查注音 Bug 作修正
--]]

  -- elseif comp:empty() then
  --   return 2

  elseif not seg:has_tag("reverse2_lookup") then
    return 2


  --- 以下修正：附加方案鍵盤範圍大於主方案時，選字時出現的 bug。
  elseif seg:has_tag("paging") and ( key:repr() == "space" or key:repr() == "Return" or key:repr() == "KP_Enter" ) then
    --- 先上屏 paging 時選擇的選項
    local cand = context:get_selected_candidate()
    engine:commit_text(cand.text)

    --- 計算末尾殘留的非中文字元數（未被選擇的 cand.input 字元數）
    local n_gct_cut = #string.gsub(g_c_t, "[^.,;/ %w-]", "")
    --- 補前綴 "="，導入未上屏編碼，避免跳回主方案
    if n_gct_cut == 0 then
      context:clear()
    else
      context.input = "=" .. string.sub(c_input, -n_gct_cut)
    end
    return 1


  --- 以下修正：附加方案鍵盤範圍大於主方案時，小板數字鍵選擇出現之 bug。
  elseif key_num then
    --- 確定選項編號
    -- 以下針對選字編碼為：1234567890
    local page_n = 10 * (seg.selected_index // 10)    -- 先確定在第幾頁
    local key_num2 = tonumber(key_num)
    if key_num2 > 0 then
      key_num2 = key_num2 - 1 + page_n
    elseif key_num2 == 0 then
      key_num2 = key_num2 - 1 + page_n + 10
    end

    --- 上屏選擇選項。
    -- local cand = context:get_selected_candidate()  -- 只是當前位置
    local cand = seg:get_candidate_at(key_num2)
    engine:commit_text(cand.text)

    -- context:select(key_num)
    -- context:confirm_current_selection()
    -- local s_index = seg.selected_index
    -- engine:commit_text(s_index)
    -- engine:commit_text(g_s_t)
    -- engine:commit_text(g_c_t)
    -- engine:commit_text(key_num2)

    --- 刪除已上屏字詞的前頭字元
    -- local cand_len = #cand.text // 3
    local cand_len = utf8.len(cand.text)
    local ci_cut = string.gsub(c_input, "^=", "")
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

    --- 補前綴 "="，導入未上屏編碼，避免跳回主方案
    if #ci_cut == 0 then
      context:clear()
    else
      context.input = "=" .. ci_cut
    end

    return 1

---------------------------------------------------------------------------

  --- 一般輸入 Return 出英文，該條限定注音 Return 一律直上中文。
  elseif key:repr() == "Return" or key:repr() == "KP_Enter" then
    engine:commit_text(g_c_t)
    context:clear()
    return 1

  --- 如果末尾為聲調則跳掉，按空白鍵，則 Rime 上屏，非 lua 作用。
  elseif string.match(c_input, "[ 3467]$") then
    return 2

  --- 補掛接反查注音不能使用空白當作一聲
  elseif key:repr() == "space" then
    context.input = c_input .. " "
    return 1

  end

  return 2
end

-- return array30up_mix
return { func = processor }