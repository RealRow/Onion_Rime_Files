--- @@ email_urlw_translator
--[[
把 recognizer 正則輸入網址使用 lua 實現，使之有選項，避免設定空白清屏時無法上屏。
該項多加「www.」
--]]
-- local function init(env)
-- end

-- local function email_urlw_translator(input, seg)
local function translate(input, seg)
  local www_in = string.match(input, "^www[.][-_0-9a-z]*[-_.0-9a-z]*$")
  local url1_in = string.match(input, "^https?:.*$")
  local url2_in = string.match(input, "^ftp:.*$")
  local url3_in = string.match(input, "^mailto:.*$")
  local url4_in = string.match(input, "^file:.*$")
  -- local www_url_in = string.match(input, "^www[.][-_0-9a-z]*[-_.0-9a-z]*$") or
  --                    string.match(input, "^https?:.*$") or
  --                    string.match(input, "^ftp:.*$") or
  --                    string.match(input, "^mailto:.*$") or
  --                    string.match(input, "^file:.*$")
  local email_in = string.match(input, "^[a-z][-_.0-9a-z]*@.*$")

  -- local url_cand = Candidate("englishtype", seg.start, seg._end, input , "〔URL〕")
  -- local email_cand = Candidate("englishtype", seg.start, seg._end, input , "〔e-mail〕")

  -- if string.match(input, "^www[.][-_0-9a-z]*[-_.0-9a-z]*$") or string.match(input, "^https?:.*$") or string.match(input, "^ftp:.*$") or string.match(input, "^mailto:.*$") or string.match(input, "^file:.*$") then
  if www_in or url1_in or url2_in or url3_in or url4_in then
  -- if www_url_in then
    yield(Candidate("englishtype", seg.start, seg._end, input , "〔URL〕"))
    -- yield(url_cand)
    -- return
  -- end
  -- elseif string.match(input, "^[a-z][-_.0-9a-z]*@.*$") then
  elseif email_in then
    yield(Candidate("englishtype", seg.start, seg._end, input , "〔e-mail〕"))
    -- yield(email_cand)
    -- return
  end

end

-- return email_urlw_translator
-- return {init = init, func = translate}
return { func = translate }