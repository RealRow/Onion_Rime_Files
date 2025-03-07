--- @@ mix_apc_s2rm 注音mixin 1_2_4 和 plus 專用
--[[
（bo_mixin 1、2、4；bopomo_onionplus）
合併 ascii_punct_change 和 s2r_most，增進效能。
--]]

-- local function mix_apc_s2rm(key, env)
local function processor(key, env)
  local engine = env.engine
  local context = engine.context
  local input_124 = context.input
  local orig_124 = context:get_commit_text()
  local o_ascii_punct = context:get_option("ascii_punct")
  local o_ascii_mode = context:get_option("ascii_mode")
  -- local check_i1 = string.match(input_124, "[@:]")
  -- local check_i2 = string.match(input_124, "'/")
  -- local check_i3 = string.match(input_124, "=[-125890;,./]$")
  -- local check_i4 = string.match(input_124, "=[-;,./][-;,./]$")
  -- local check_i5 = string.match(input_124, "==[90]$")
  local check_i = string.match(input_124, "[@:]") or
                  string.match(input_124, "'/") or
                  string.match(input_124, "=[-125890;,./]$") or
                  string.match(input_124, "=[-;,./][-;,./]$") or
                  string.match(input_124, "==[90]$")
  -- local c_i_c = context:is_composing()

  if o_ascii_mode then
    return 2

  elseif key:repr() == "space" and context:is_composing() then
  -- elseif key:repr() == "space" and context:has_menu() then
  -- elseif key:repr() == "space" and c_i_c then
  -- elseif (key:repr() == "space") then
    if check_i then
    -- if check_i1 or check_i2 or check_i3 or check_i4 or check_i5 then
    -- if ( string.match(input_124, "[@:]") or string.match(input_124, "'/") or string.match(input_124, "=[-125890;,./]$") or string.match(input_124, "=[-;,./][-;,./]$") or string.match(input_124, "==[90]$") ) then  --or string.match(input_124, "==[,.]{2}$")
    -- if ( string.match(input_124, "[@:]") or string.match(input_124, "'/") or string.match(input_124, "=[-125890;,./]$") or string.match(input_124, "=[-;,./][-;,./]$") or string.match(input_124, "==[90]$") or string.match(input_124, "==[,][,]?$") or string.match(input_124, "==[.][.]?$") ) then
    -- -- 「全，非精簡」 if ( string.match(input_124, "[@:]") or string.match(input_124, "'/") or string.match(input_124, "=[-125890;,./]$") or string.match(input_124, "=[-][-]$") or string.match(input_124, "=[;][;]$") or string.match(input_124, "=[,][,]$") or string.match(input_124, "=[.][.]$") or string.match(input_124, "=[/][/]$") or string.match(input_124, "==[90]$") or string.match(input_124, "==[,][,]?$") or string.match(input_124, "==[.][.]?$") ) then
      engine:commit_text(orig_124)
      context:clear()
      return 1 -- kAccepted
    end

  elseif o_ascii_punct then
    if key:repr() == "Shift+less" then
      if context:is_composing() then
      -- if c_i_c then
        engine:commit_text( orig_124 .. "," )
      else
        engine:commit_text( "," )
      end
      context:clear()
      return 1 -- kAccepted
    elseif key:repr() == "Shift+greater" then
      if context:is_composing() then
      -- if c_i_c then
        engine:commit_text( orig_124 .. "." )
      else
        engine:commit_text( "." )
      end
      context:clear()
      return 1 -- kAccepted
    end

  end

  return 2 -- kNoop
end

-- return mix_apc_s2rm
return { func = processor }