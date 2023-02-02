--- @@ instruction_dbpmf
--[[
說明雙拼注音各種掛接
--]]
local function init(env)
  env.table_sd_1 = {
        { ' ※ 輸入【項目】每字第一個注音，調出相關符號。', '𝟎' }
      , { '【表情】【自然】【飲食】【活動】【旅遊】【物品】', '𝟏' }
      , { '【符號】【國旗】【微笑】【大笑】【冒汗】【喜愛】', '𝟐' }
      , { '【討厭】【無奈】【哭泣】【冷淡】【驚訝】【生氣】', '𝟑' }
      , { '【懷疑】【大頭】【人物】【獸面】【貓頭】【怪物】', '𝟒' }
      , { '【五官】【手勢】【亞裔】【白人】【黑人】【天氣】', '𝟓' }
      , { '【下雪】【天體】【夜空】【地球】【景色】【景點】', '𝟔' }
      , { '【名勝】【日本】【美國】【法國】【建築】【節日】', '𝟕' }
      , { '【娛樂】【遊戲】【運動】【球具】【獎項】【獎牌】', '𝟖' }
      , { '【食物】【正飯】【午餐】【早餐】【早點】【中餐】', '𝟗' }
      , { '【西餐】【快餐】【速食】【米飯】【麵包】【捲物】', '𝟏𝟎' }
      , { '【串物】【甜點】【零食】【飲料】【熱飲】【酒精】', '𝟏𝟏' }
      , { '【酒類】【植物】【水果】【蔬菜】【粗糧】【花卉】', '𝟏𝟐' }
      , { '【葉子】【肉類】【肉品】【牲畜】【畜牲】【禽類】', '𝟏𝟑' }
      , { '【鳥類】【魚圖】【鳥圖】【蟲圖】【器官】【日用】', '𝟏𝟒' }
      , { '【血液】【服裝】【衣物】【衣服】【褲子】【帽子】', '𝟏𝟓' }
      , { '【包包】【頭髮】【膚色】【化妝】【愛情】【愛心】', '𝟏𝟔' }
      , { '【兩性】【效果】【色塊】【宗教】【音樂】【樂器】', '𝟏𝟕' }
      , { '【時鐘】【標誌】【圖示】【圖標】【箭標】【指示】', '𝟏𝟖' }
      , { '【回收】【有害】【科學】【通訊】【電腦】【工業】', '𝟏𝟗' }
      , { '【電子】【武器】【象棋】【麻將】【骰子】【撲克】', '𝟐𝟎' }
      , { '【船隻】【飛機】【汽車】【車輛】【公交】【城軌】', '𝟐𝟏' }
      , { '【捷運】【火車】【錢財】【鈔票】【紙鈔】【紙幣】', '𝟐𝟐' }
      , { '【貨幣】【單位】【數學】【分數】【打勾】【星號】', '𝟐𝟑' }
      , { '【箭頭】【線段】【幾何】【三角】【方塊】【圓形】', '𝟐𝟒' }
      , { '【填色】【文化】【占星】【星座】【易經】【八卦】', '𝟐𝟓' }
      , { '【卦名】【天干】【地支】【干支】【節氣】【月份】', '𝟐𝟔' }
      , { '【日期】【曜日】【時間】【符碼】【標點】【合字】', '𝟐𝟕' }
      , { '【部首】【偏旁】【筆畫】【倉頡】【結構】【拼音】', '𝟐𝟖' }
      , { '【注音】【聲調】【上標】【下標】【羅馬】【希臘】', '𝟐𝟗' }
      , { '【俄語】【韓文】【(平)假名】', '𝟑𝟎' }
      , { '【幾何圖】【鞋子圖】【眼鏡圖】【工具圖】【電器圖】', '𝟑𝟏' }
      , { '【甜食圖】【餐具圖】【動物圖】【生肖圖】【家禽圖】', '𝟑𝟐' }
      , { '【魚類圖】【蟲類圖】【血型圖】【精怪圖】【月相圖】', '𝟑𝟑' }
      , { '【交通圖】【飛行器】【多媒體】【黃種人】【拉美裔】', '𝟑𝟒' }
      , { '【棕色人】【白種人】【阿拉伯】【動物臉】【猴子頭】', '𝟑𝟓' }
      , { '【咧嘴笑】【做運動】【日本菜】【食物捲】【辦公室】', '𝟑𝟔' }
      , { '【警消護】【大自然】【遊樂園】【撲克牌】【西洋棋】', '𝟑𝟕' }
      , { '【輸入法】【日用品】【單線框】【雙線框】【色塊心】', '𝟑𝟖' }
      , { '【色塊方】【色塊圓】【十字架】【星座名】【十二宮】', '𝟑𝟗' }
      , { '【太玄經】【蘇州碼】【標點直】【羅馬大】【希臘大】', '𝟒𝟎' }
      , { '【俄語大】【字母圈】【字母括】【字母方】【字母框】', '𝟒𝟏' }
      , { '【數字圈】【數字括】【數字點】【數字標】【漢字圈】', '𝟒𝟐' }
      , { '【漢字框】【漢字括】【韓文圈】【韓文括】【假名圈】', '𝟒𝟑' }
      , { '【日本年】【填色塊】【假名半(形)】', '𝟒𝟒' }
      , { '【IRO(いろは順)】', '𝟒𝟓' }
      , { '【猴子表情】【十二生肖】【交通工具】【公共運輸】', '𝟒𝟔' }
      , { '【野生動物】【日式料理】【日本料理】【日本星期】', '𝟒𝟕' }
      , { '【羅馬數字】【數字圈黑】【數字黑圈】【字母圈大】', '𝟒𝟖' }
      , { '【字母括大】【字母黑圈】【字母圈黑】【字母黑方】', '𝟒𝟗' }
      , { '【字母方黑】【字母框黑】【字母黑框】【易經卦名】', '𝟓𝟎' }
      , { '【六十四卦】【六十四卦名】【羅馬數字大】', '𝟓𝟏' }
      , { '【PM(片)假名】【運動NY(女)】【運動NH(男)】', '𝟓𝟐' }
      , { '【精怪NY(女)】【精怪NH(男)】', '𝟓𝟑' }
      , { '【 a 假名】【 i 假名】【 u 假名】【 e 假名】【 o 假名】', '𝟓𝟒' }
      , { '【 k 假名】【 g 假名】【 s 假名】【 z 假名】【 t 假名】', '𝟓𝟓' }
      , { '【 d 假名】【 n 假名】【 h 假名】【 b 假名】【 p 假名】', '𝟓𝟔' }
      , { '【 m 假名】【 y 假名】【 r 假名】【 w 假名】', '𝟓𝟕' }
      , { ' ｢圈｣｢框｣｢括｣數字字母：【 0 ~ 10 】【 1-0 ~ 5-0 】【 a ~ z 】', '𝟓𝟖' }
  }
  env.table_sd_2 = {
        { '〖 a ~ z 〗字母變化      ※ 以下 顏文字：', '𝟘' }
      , { '〖 1 〗開心 〖 2 〗喜歡 〖 3 〗傷心', '𝟙' }
      , { '〖 4 〗生氣 〖 5 〗驚訝 〖 6 〗無奈', '𝟚' }
      , { '〖 7 〗喜     〖 8 〗樂     〖 9 〗怒', '𝟛' }
      , { '〖 0 〗指示和圖示          〖 - 〗回話', '𝟜' }
  }
  env.table_sd_3 = {
        { 'ㄅⒷ ㄆⓟ ㄇⓂ ㄈⒻ ｜ ㄉⒹ ㄊⓉ ㄋⓃ ㄌⓁ ｜ ㄍⒼ ㄎⓀ ㄏⒽ', '⓿' }
      , { 'ㄐⒿ ㄑⓆ ㄒⓍ ｜ㄓⓌ ㄔⓋ ㄕⒶ ㄖⓇ ｜ ㄗⓏ ㄘⒸ ㄙⓈ', '❶' }
      , { 'ㄧⒾ ㄨⓊ ㄩⓎ　　　《 空韻： ㄭⒾ　(ㄧㄨㄩ)ㄭⒺ　◌Ⓞ 》', '❷' }
      , { 'ㄚⒶ ㄛⓄ ㄜⒺ ㄝⓀ ｜ ㄞⒿ ㄟⓀ ㄠⓌ ㄡⒹ', '❸' }
      , { 'ㄢⒽ ㄣⒻ ㄤⓈ ㄥⒼ ｜ ㄦⓇ', '❹' }
      , { 'ㄧㄚⓏ ㄧㄝⓟ ㄧㄠⓆ ㄧㄡⒸ ㄧㄢⓂ ㄧㄣⓇ ㄧㄤⓍ ㄧㄥⓉ', '❺' }
      , { 'ㄨㄚⓏ ㄨㄛⓄ ㄨㄞⓂ ㄨㄟⓁ ㄨㄢⓃ ㄨㄣⓋ ㄨㄤⓍ ㄨㄥⒷ', '❻' }
      , { 'ㄩㄝⓁ ㄩㄢⓃ ㄩㄣⓋ ㄩㄥⒷ', '❼' }
      , { '一聲 ˉ =（ ; ） 二聲 ˊ =（ / ） 三聲 ˇ =（ , ） 四聲 ˋ =（ \' ）', '❽' }
      , { '輕聲 ˙ = （ . ）', '❾' }
  }
end

-- local function instruction_dbpmf(input, seg, env)
local function translate(input, seg, env)
  engine = env.engine
  context = engine.context
  caret_pos = context.caret_pos
  -- local check_semicolon = string.match(input, "^;$")
  -- local check_semicolon2 = string.match(input, "^;;$")
  -- local check_e = string.match(input, "^e$")

  -- if input:find('^;$') then
  -- if check_semicolon and caret_pos == 1 then
  if input == ";" and caret_pos == 1 then
    -- for cand in input:iter() do
    --   yield(cand)
    -- end
    for k, v in ipairs(env.table_sd_1) do
      local cand = Candidate('help', seg.start, seg._end, v[2], ' ' .. v[1])
      -- cand.preedit = input .. '\t※ 輸入【項目】每字第一個注音，調出相關符號。'
      yield(cand)
    end
  end

  -- if input:find('^;;$') then
  -- if check_semicolon2 and caret_pos == 2 then
  if input == ";;" and caret_pos == 2 then
    for k, v in ipairs(env.table_sd_2) do
      local cand = Candidate('help', seg.start, seg._end, v[2], ' ' .. v[1])
      -- cand.preedit = input .. '\t※ 輸入【項目】每字第一個注音，調出相關符號。'
      yield(cand)
    end
  end

  -- if input:find('^e$') then
  -- if check_e and caret_pos == 1 then
  if input == "e" and caret_pos == 1 then
    for k, v in ipairs(env.table_sd_3) do
      local cand = Candidate('help', seg.start, seg._end, v[2], ' ' .. v[1])
      cand.preedit = input .. '\t《查詢鍵位注音》▶'
      yield(cand)
    end
  end

end

-- return instruction_dbpmf
return {init = init, func = translate}