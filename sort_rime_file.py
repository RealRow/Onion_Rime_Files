
import os
import shutil
import time

#※新增資料夾(多層目錄, 如前一層data資料夾不存在, 將自動新增)※
os.makedirs('./sort_rime/注音洋蔥純注音版/', exist_ok=True)
os.makedirs('./sort_rime/注音洋蔥雙拼版/', exist_ok=True)
os.makedirs('./sort_rime/注音洋蔥mixin版/opencc/', exist_ok=True)
os.makedirs('./sort_rime/注音洋蔥plus版/opencc/', exist_ok=True)
os.makedirs('./sort_rime/地球拼音洋蔥mix-in版/opencc/', exist_ok=True)
os.makedirs('./sort_rime/ocm/ocm_mixin/opencc/', exist_ok=True)
os.makedirs('./sort_rime/ocm/ocm_plus/opencc/', exist_ok=True)


#複製檔案(注音洋蔥純注音版)
shutil.copyfile("./allfiles/essay-zh-hant-onion.txt", "./sort_rime/注音洋蔥純注音版/essay-zh-hant-onion.txt")
shutil.copyfile("./allfiles/bopomo_onion_phrase.txt", "./sort_rime/注音洋蔥純注音版/bopomo_onion_phrase.txt")
shutil.copyfile("./allfiles/bopomo_onion_symbols.yaml", "./sort_rime/注音洋蔥純注音版/bopomo_onion_symbols.yaml")
shutil.copyfile("./allfiles/bopomo_onion.extended.dict.yaml", "./sort_rime/注音洋蔥純注音版/bopomo_onion.extended.dict.yaml")
shutil.copyfile("./allfiles/bopomo_onion.schema.yaml", "./sort_rime/注音洋蔥純注音版/bopomo_onion.schema.yaml")
shutil.copyfile("./allfiles/cangjie5.dict.yaml", "./sort_rime/注音洋蔥純注音版/cangjie5.dict.yaml")
shutil.copyfile("./allfiles/cangjie5.schema.yaml", "./sort_rime/注音洋蔥純注音版/cangjie5.schema.yaml")
shutil.copyfile("./allfiles/terra_pinyin_onion_add.dict.yaml", "./sort_rime/注音洋蔥純注音版/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./allfiles/terra_pinyin_onion.dict.yaml", "./sort_rime/注音洋蔥純注音版/terra_pinyin_onion.dict.yaml")

shutil.copyfile("./allfiles/各方案default.custom/注音洋蔥純注音版_custom/default.custom.yaml", "./sort_rime/注音洋蔥純注音版/default.custom.yaml")


#複製檔案(注音洋蔥雙拼版版)
shutil.copyfile("./allfiles/essay-zh-hant-onion.txt", "./sort_rime/注音洋蔥雙拼版/essay-zh-hant-onion.txt")
shutil.copyfile("./allfiles/bopomo_onion_double.extended.dict.yaml", "./sort_rime/注音洋蔥雙拼版/bopomo_onion_double.extended.dict.yaml")
shutil.copyfile("./allfiles/bopomo_onion_double.schema.yaml", "./sort_rime/注音洋蔥雙拼版/bopomo_onion_double.schema.yaml")
shutil.copyfile("./allfiles/cangjie5.dict.yaml", "./sort_rime/注音洋蔥雙拼版/cangjie5.dict.yaml")
shutil.copyfile("./allfiles/cangjie5.schema.yaml", "./sort_rime/注音洋蔥雙拼版/cangjie5.schema.yaml")
shutil.copyfile("./allfiles/rime.lua", "./sort_rime/注音洋蔥雙拼版/rime.lua")
shutil.copyfile("./allfiles/terra_pinyin_onion_add.dict.yaml", "./sort_rime/注音洋蔥雙拼版/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./allfiles/terra_pinyin_onion.dict.yaml", "./sort_rime/注音洋蔥雙拼版/terra_pinyin_onion.dict.yaml")
shutil.copyfile("./allfiles/symbols_bpmf.dict.yaml", "./sort_rime/注音洋蔥雙拼版/symbols_bpmf.dict.yaml")
shutil.copyfile("./allfiles/symbols_double_bpmf.schema.yaml", "./sort_rime/注音洋蔥雙拼版/symbols_double_bpmf.schema.yaml")

shutil.copyfile("./allfiles/各方案default.custom/注音洋蔥雙拼版_custom/default.custom.yaml", "./sort_rime/注音洋蔥雙拼版/default.custom.yaml")

shutil.copytree('./allfiles/雙拼注音不開頭簡拼custom/', './sort_rime/注音洋蔥雙拼版/雙拼注音不開頭簡拼custom/')
shutil.copytree('./allfiles/雙拼注音鍵位說明圖示/', './sort_rime/注音洋蔥雙拼版/雙拼注音鍵位說明圖示/')


#複製檔案(注音洋蔥mixin版)
shutil.copyfile("./allfiles/essay-zh-hant-onion.txt", "./sort_rime/注音洋蔥mixin版/essay-zh-hant-onion.txt")
shutil.copyfile("./allfiles/essay-jp-onion.txt", "./sort_rime/注音洋蔥mixin版/essay-jp-onion.txt")
shutil.copyfile("./allfiles/allbpm.dict.yaml", "./sort_rime/注音洋蔥mixin版/allbpm.dict.yaml")
shutil.copyfile("./allfiles/allbpm.schema.yaml", "./sort_rime/注音洋蔥mixin版/allbpm.schema.yaml")
shutil.copyfile("./allfiles/bo_mixin_jp.dict.yaml", "./sort_rime/注音洋蔥mixin版/bo_mixin_jp.dict.yaml")
shutil.copyfile("./allfiles/bo_mixin_kr.dict.yaml", "./sort_rime/注音洋蔥mixin版/bo_mixin_kr.dict.yaml")
shutil.copyfile("./allfiles/bo_mixin_la.dict.yaml", "./sort_rime/注音洋蔥mixin版/bo_mixin_la.dict.yaml")
shutil.copyfile("./allfiles/bo_mixin_phrase.txt", "./sort_rime/注音洋蔥mixin版/bo_mixin_phrase.txt")
shutil.copyfile("./allfiles/bo_mixin.extended.dict.yaml", "./sort_rime/注音洋蔥mixin版/bo_mixin.extended.dict.yaml")
shutil.copyfile("./allfiles/bo_mixin1.schema.yaml", "./sort_rime/注音洋蔥mixin版/bo_mixin1.schema.yaml")
shutil.copyfile("./allfiles/bo_mixin2.schema.yaml", "./sort_rime/注音洋蔥mixin版/bo_mixin2.schema.yaml")
shutil.copyfile("./allfiles/bo_mixin3.schema.yaml", "./sort_rime/注音洋蔥mixin版/bo_mixin3.schema.yaml")
shutil.copyfile("./allfiles/cangjie5.dict.yaml", "./sort_rime/注音洋蔥mixin版/cangjie5.dict.yaml")
shutil.copyfile("./allfiles/cangjie5.schema.yaml", "./sort_rime/注音洋蔥mixin版/cangjie5.schema.yaml")
shutil.copyfile("./allfiles/cyrillic.dict.yaml", "./sort_rime/注音洋蔥mixin版/cyrillic.dict.yaml")
shutil.copyfile("./allfiles/cyrillic.extended.dict.yaml", "./sort_rime/注音洋蔥mixin版/cyrillic.extended.dict.yaml")
shutil.copyfile("./allfiles/cyrillic.schema.yaml", "./sort_rime/注音洋蔥mixin版/cyrillic.schema.yaml")
shutil.copyfile("./allfiles/easy_en_b.dict.yaml", "./sort_rime/注音洋蔥mixin版/easy_en_b.dict.yaml")
shutil.copyfile("./allfiles/easy_en_b.schema.yaml", "./sort_rime/注音洋蔥mixin版/easy_en_b.schema.yaml")
shutil.copyfile("./allfiles/easy_en_comment.dict.yaml", "./sort_rime/注音洋蔥mixin版/easy_en_comment.dict.yaml")
shutil.copyfile("./allfiles/easy_en_comment.schema.yaml", "./sort_rime/注音洋蔥mixin版/easy_en_comment.schema.yaml")
shutil.copyfile("./allfiles/element_bopomo.yaml", "./sort_rime/注音洋蔥mixin版/element_bopomo.yaml")
shutil.copyfile("./allfiles/fullshape.extended.dict.yaml", "./sort_rime/注音洋蔥mixin版/fullshape.extended.dict.yaml")
shutil.copyfile("./allfiles/fullshape.dict.yaml", "./sort_rime/注音洋蔥mixin版/fullshape.dict.yaml")
shutil.copyfile("./allfiles/fullshape.schema.yaml", "./sort_rime/注音洋蔥mixin版/fullshape.schema.yaml")
shutil.copyfile("./allfiles/greek.dict.yaml", "./sort_rime/注音洋蔥mixin版/greek.dict.yaml")
shutil.copyfile("./allfiles/greek.extended.dict.yaml", "./sort_rime/注音洋蔥mixin版/greek.extended.dict.yaml")
shutil.copyfile("./allfiles/greek.schema.yaml", "./sort_rime/注音洋蔥mixin版/greek.schema.yaml")

shutil.copyfile("./allfiles/phrases.cht_en_w.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.cht_en_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.cht.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.cht.dict.yaml")
shutil.copyfile("./allfiles/phrases.chtp.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.chtp.dict.yaml")
shutil.copyfile("./allfiles/phrases.chtpp.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.chtpp.dict.yaml")
shutil.copyfile("./allfiles/phrases.cyr_all.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.cyr_all.dict.yaml")
shutil.copyfile("./allfiles/phrases.en_l_w.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.en_l_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.en_o_w.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.en_o_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.en_u_w.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.en_u_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.fs_all.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.fs_all.dict.yaml")
shutil.copyfile("./allfiles/phrases.gr_all.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.gr_all.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hk_more.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.jp_hk_more.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hk.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.jp_hk.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hkkreduce.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.jp_hkkreduce.dict.yaml")
shutil.copyfile("./allfiles/phrases.kr_more.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.kr_more.dict.yaml")
shutil.copyfile("./allfiles/phrases.kr.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.kr.dict.yaml")
shutil.copyfile("./allfiles/phrases.la_py_w.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.la_py_w.dict.yaml")

shutil.copyfile("./allfiles/punct_bopomo.yaml", "./sort_rime/注音洋蔥mixin版/punct_bopomo.yaml")
shutil.copyfile("./allfiles/rime.lua", "./sort_rime/注音洋蔥mixin版/rime.lua")
shutil.copyfile("./allfiles/symbols_bpmf.dict.yaml", "./sort_rime/注音洋蔥mixin版/symbols_bpmf.dict.yaml")
shutil.copyfile("./allfiles/symbols_bpmf.schema.yaml", "./sort_rime/注音洋蔥mixin版/symbols_bpmf.schema.yaml")
shutil.copyfile("./allfiles/terra_pinyin_onion_add.dict.yaml", "./sort_rime/注音洋蔥mixin版/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./allfiles/terra_pinyin_onion.dict.yaml", "./sort_rime/注音洋蔥mixin版/terra_pinyin_onion.dict.yaml")

shutil.copyfile("./allfiles/jpnin1_phrase.txt", "./sort_rime/注音洋蔥mixin版/jpnin1_phrase.txt")
shutil.copyfile("./allfiles/jpnin1.dict.yaml", "./sort_rime/注音洋蔥mixin版/jpnin1.dict.yaml")
shutil.copyfile("./allfiles/jpnin1.extended.dict.yaml", "./sort_rime/注音洋蔥mixin版/jpnin1.extended.dict.yaml")
shutil.copyfile("./allfiles/jpnin1.schema.yaml", "./sort_rime/注音洋蔥mixin版/jpnin1.schema.yaml")
shutil.copyfile("./allfiles/phrases.jp_hkk.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.jp_hkk.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hkkseg.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.jp_hkkseg.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hkup_w.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.jp_hkup_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hkmoreup_w.dict.yaml", "./sort_rime/注音洋蔥mixin版/phrases.jp_hkmoreup_w.dict.yaml")

shutil.copyfile("./allfiles/各方案default.custom/注音洋蔥mixin版_custom/default.custom.yaml", "./sort_rime/注音洋蔥mixin版/default.custom.yaml")

shutil.copyfile("./allfiles/opencc/back_mark.json", "./sort_rime/注音洋蔥mixin版/opencc/back_mark.json")
shutil.copyfile("./allfiles/opencc/back_mark.txt", "./sort_rime/注音洋蔥mixin版/opencc/back_mark.txt")
shutil.copyfile("./allfiles/opencc/bpm_big5e_hkscs_jis.json", "./sort_rime/注音洋蔥mixin版/opencc/bpm_big5e_hkscs_jis.json")
shutil.copyfile("./allfiles/opencc/bpm_big5e_hkscs_jis.txt", "./sort_rime/注音洋蔥mixin版/opencc/bpm_big5e_hkscs_jis.txt")
shutil.copyfile("./allfiles/opencc/emoji.json", "./sort_rime/注音洋蔥mixin版/opencc/emoji.json")
shutil.copyfile("./allfiles/opencc/emoji.txt", "./sort_rime/注音洋蔥mixin版/opencc/emoji.txt")
shutil.copyfile("./allfiles/opencc/ocm_big5e_hkscs_jis.json", "./sort_rime/注音洋蔥mixin版/opencc/ocm_big5e_hkscs_jis.json")
shutil.copyfile("./allfiles/opencc/ocm_big5e_hkscs_jis.txt", "./sort_rime/注音洋蔥mixin版/opencc/ocm_big5e_hkscs_jis.txt")
shutil.copyfile("./allfiles/opencc/punct_mark.json", "./sort_rime/注音洋蔥mixin版/opencc/punct_mark.json")
shutil.copyfile("./allfiles/opencc/punct_mark.txt", "./sort_rime/注音洋蔥mixin版/opencc/punct_mark.txt")

shutil.copytree('./allfiles/mixin注音_同顯1修改檔(Mac)/', './sort_rime/注音洋蔥mixin版/mixin注音_同顯1修改檔(Mac)/')
shutil.copytree('./allfiles/mixin注音_同顯2修改檔(Mac)/', './sort_rime/注音洋蔥mixin版/mixin注音_同顯2修改檔(Mac)/')
shutil.copytree('./allfiles/mixin注音_同顯1修改檔(Win)/', './sort_rime/注音洋蔥mixin版/mixin注音_同顯1修改檔(Win)/')
shutil.copytree('./allfiles/mixin注音_同顯2修改檔(Win)/', './sort_rime/注音洋蔥mixin版/mixin注音_同顯2修改檔(Win)/')


#複製檔案(注音洋蔥plus版)
shutil.copyfile("./allfiles/essay-zh-hant-onion.txt", "./sort_rime/注音洋蔥plus版/essay-zh-hant-onion.txt")
shutil.copyfile("./allfiles/essay-jp-onion.txt", "./sort_rime/注音洋蔥plus版/essay-jp-onion.txt")
shutil.copyfile("./allfiles/allbpm.dict.yaml", "./sort_rime/注音洋蔥plus版/allbpm.dict.yaml")
shutil.copyfile("./allfiles/allbpm.schema.yaml", "./sort_rime/注音洋蔥plus版/allbpm.schema.yaml")
shutil.copyfile("./allfiles/bopomo_onionplus_2.schema.yaml", "./sort_rime/注音洋蔥plus版/bopomo_onionplus_2.schema.yaml")
shutil.copyfile("./allfiles/bopomo_onionplus_phrase.txt", "./sort_rime/注音洋蔥plus版/bopomo_onionplus_phrase.txt")
shutil.copyfile("./allfiles/bopomo_onionplus.extended.dict.yaml", "./sort_rime/注音洋蔥plus版/bopomo_onionplus.extended.dict.yaml")
shutil.copyfile("./allfiles/bopomo_onionplus.schema.yaml", "./sort_rime/注音洋蔥plus版/bopomo_onionplus.schema.yaml")
shutil.copyfile("./allfiles/cangjie5.dict.yaml", "./sort_rime/注音洋蔥plus版/cangjie5.dict.yaml")
shutil.copyfile("./allfiles/cangjie5.schema.yaml", "./sort_rime/注音洋蔥plus版/cangjie5.schema.yaml")
shutil.copyfile("./allfiles/cyrillic.dict.yaml", "./sort_rime/注音洋蔥plus版/cyrillic.dict.yaml")
shutil.copyfile("./allfiles/cyrillic.extended.dict.yaml", "./sort_rime/注音洋蔥plus版/cyrillic.extended.dict.yaml")
shutil.copyfile("./allfiles/cyrillic.schema.yaml", "./sort_rime/注音洋蔥plus版/cyrillic.schema.yaml")
shutil.copyfile("./allfiles/easy_en_b.dict.yaml", "./sort_rime/注音洋蔥plus版/easy_en_b.dict.yaml")
shutil.copyfile("./allfiles/easy_en_b.schema.yaml", "./sort_rime/注音洋蔥plus版/easy_en_b.schema.yaml")
shutil.copyfile("./allfiles/easy_en_comment.dict.yaml", "./sort_rime/注音洋蔥plus版/easy_en_comment.dict.yaml")
shutil.copyfile("./allfiles/easy_en_comment.schema.yaml", "./sort_rime/注音洋蔥plus版/easy_en_comment.schema.yaml")
shutil.copyfile("./allfiles/element_bopomo.yaml", "./sort_rime/注音洋蔥plus版/element_bopomo.yaml")
shutil.copyfile("./allfiles/fullshape.extended.dict.yaml", "./sort_rime/注音洋蔥plus版/fullshape.extended.dict.yaml")
shutil.copyfile("./allfiles/fullshape.dict.yaml", "./sort_rime/注音洋蔥plus版/fullshape.dict.yaml")
shutil.copyfile("./allfiles/fullshape.schema.yaml", "./sort_rime/注音洋蔥plus版/fullshape.schema.yaml")
shutil.copyfile("./allfiles/greek.dict.yaml", "./sort_rime/注音洋蔥plus版/greek.dict.yaml")
shutil.copyfile("./allfiles/greek.extended.dict.yaml", "./sort_rime/注音洋蔥plus版/greek.extended.dict.yaml")
shutil.copyfile("./allfiles/greek.schema.yaml", "./sort_rime/注音洋蔥plus版/greek.schema.yaml")
shutil.copyfile("./allfiles/hangeul_phrase.txt", "./sort_rime/注音洋蔥plus版/hangeul_phrase.txt")
shutil.copyfile("./allfiles/hangeul.dict.yaml", "./sort_rime/注音洋蔥plus版/hangeul.dict.yaml")
shutil.copyfile("./allfiles/hangeul.extended.dict.yaml", "./sort_rime/注音洋蔥plus版/hangeul.extended.dict.yaml")
shutil.copyfile("./allfiles/hangeul.schema.yaml", "./sort_rime/注音洋蔥plus版/hangeul.schema.yaml")
shutil.copyfile("./allfiles/jpnin1_phrase.txt", "./sort_rime/注音洋蔥plus版/jpnin1_phrase.txt")
shutil.copyfile("./allfiles/jpnin1.dict.yaml", "./sort_rime/注音洋蔥plus版/jpnin1.dict.yaml")
shutil.copyfile("./allfiles/jpnin1.extended.dict.yaml", "./sort_rime/注音洋蔥plus版/jpnin1.extended.dict.yaml")
shutil.copyfile("./allfiles/jpnin1.schema.yaml", "./sort_rime/注音洋蔥plus版/jpnin1.schema.yaml")
shutil.copyfile("./allfiles/jpnin1.custom.yaml", "./sort_rime/注音洋蔥plus版/jpnin1.custom.yaml")
shutil.copyfile("./allfiles/latinin1.dict.yaml", "./sort_rime/注音洋蔥plus版/latinin1.dict.yaml")
shutil.copyfile("./allfiles/latinin1.extended.dict.yaml", "./sort_rime/注音洋蔥plus版/latinin1.extended.dict.yaml")
shutil.copyfile("./allfiles/latinin1.schema.yaml", "./sort_rime/注音洋蔥plus版/latinin1.schema.yaml")

shutil.copyfile("./allfiles/phrases.cht.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.cht.dict.yaml")
shutil.copyfile("./allfiles/phrases.chtp.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.chtp.dict.yaml")
shutil.copyfile("./allfiles/phrases.chtpp.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.chtpp.dict.yaml")
shutil.copyfile("./allfiles/phrases.cyr_all.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.cyr_all.dict.yaml")
shutil.copyfile("./allfiles/phrases.en_l_w.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.en_l_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.en_o_w.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.en_o_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.en_u_w.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.en_u_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.fs_all.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.fs_all.dict.yaml")
shutil.copyfile("./allfiles/phrases.gr_all.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.gr_all.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hk.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.jp_hk.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hk_more.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.jp_hk_more.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hkk.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.jp_hkk.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hkkseg.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.jp_hkkseg.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hkup_w.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.jp_hkup_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hkmoreup_w.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.jp_hkmoreup_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.kr_more.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.kr_more.dict.yaml")
shutil.copyfile("./allfiles/phrases.la_py_w.dict.yaml", "./sort_rime/注音洋蔥plus版/phrases.la_py_w.dict.yaml")

shutil.copyfile("./allfiles/punct_bopomo.yaml", "./sort_rime/注音洋蔥plus版/punct_bopomo.yaml")
shutil.copyfile("./allfiles/rime.lua", "./sort_rime/注音洋蔥plus版/rime.lua")
shutil.copyfile("./allfiles/symbols_bpmf.dict.yaml", "./sort_rime/注音洋蔥plus版/symbols_bpmf.dict.yaml")
shutil.copyfile("./allfiles/symbols_bpmf.schema.yaml", "./sort_rime/注音洋蔥plus版/symbols_bpmf.schema.yaml")
shutil.copyfile("./allfiles/terra_pinyin_onion_add.dict.yaml", "./sort_rime/注音洋蔥plus版/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./allfiles/terra_pinyin_onion.dict.yaml", "./sort_rime/注音洋蔥plus版/terra_pinyin_onion.dict.yaml")

shutil.copyfile("./allfiles/各方案default.custom/注音洋蔥plus版_custom/default.custom.yaml", "./sort_rime/注音洋蔥plus版/default.custom.yaml")

shutil.copyfile("./allfiles/opencc/back_mark.json", "./sort_rime/注音洋蔥plus版/opencc/back_mark.json")
shutil.copyfile("./allfiles/opencc/back_mark.txt", "./sort_rime/注音洋蔥plus版/opencc/back_mark.txt")
shutil.copyfile("./allfiles/opencc/bpm_big5e_hkscs_jis.json", "./sort_rime/注音洋蔥plus版/opencc/bpm_big5e_hkscs_jis.json")
shutil.copyfile("./allfiles/opencc/bpm_big5e_hkscs_jis.txt", "./sort_rime/注音洋蔥plus版/opencc/bpm_big5e_hkscs_jis.txt")
shutil.copyfile("./allfiles/opencc/emoji.json", "./sort_rime/注音洋蔥plus版/opencc/emoji.json")
shutil.copyfile("./allfiles/opencc/emoji.txt", "./sort_rime/注音洋蔥plus版/opencc/emoji.txt")
shutil.copyfile("./allfiles/opencc/ocm_big5e_hkscs_jis.json", "./sort_rime/注音洋蔥plus版/opencc/ocm_big5e_hkscs_jis.json")
shutil.copyfile("./allfiles/opencc/ocm_big5e_hkscs_jis.txt", "./sort_rime/注音洋蔥plus版/opencc/ocm_big5e_hkscs_jis.txt")
shutil.copyfile("./allfiles/opencc/punct_mark.json", "./sort_rime/注音洋蔥plus版/opencc/punct_mark.json")
shutil.copyfile("./allfiles/opencc/punct_mark.txt", "./sort_rime/注音洋蔥plus版/opencc/punct_mark.txt")

shutil.copytree('./allfiles/plus注音_防崩潰：Win必加，Mac勿加/', './sort_rime/注音洋蔥plus版/plus注音_防崩潰：Win必加，Mac勿加/')


#複製檔案(地球拼音洋蔥mix-in版)
shutil.copyfile("./allfiles/essay-zh-hant-onion.txt", "./sort_rime/地球拼音洋蔥mix-in版/essay-zh-hant-onion.txt")
shutil.copyfile("./allfiles/cangjie5.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/cangjie5.dict.yaml")
shutil.copyfile("./allfiles/cangjie5.schema.yaml", "./sort_rime/地球拼音洋蔥mix-in版/cangjie5.schema.yaml")
shutil.copyfile("./allfiles/ocm_mixin_jp.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/ocm_mixin_jp.dict.yaml")
shutil.copyfile("./allfiles/ocm_mixin_kr.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/ocm_mixin_kr.dict.yaml")
shutil.copyfile("./allfiles/ocm_mixin_la.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/ocm_mixin_la.dict.yaml")

shutil.copyfile("./allfiles/phrases.cht_en_w.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/phrases.cht_en_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.cht.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/phrases.cht.dict.yaml")
shutil.copyfile("./allfiles/phrases.chtp.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/phrases.chtp.dict.yaml")
shutil.copyfile("./allfiles/phrases.chtpp.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/phrases.chtpp.dict.yaml")
shutil.copyfile("./allfiles/phrases.en_l_w.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/phrases.en_l_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.en_o_w.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/phrases.en_o_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.en_u_w.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/phrases.en_u_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hk.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/phrases.jp_hk.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hkkreduce.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/phrases.jp_hkkreduce.dict.yaml")
shutil.copyfile("./allfiles/phrases.kr.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/phrases.kr.dict.yaml")
shutil.copyfile("./allfiles/phrases.la_py_w.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/phrases.la_py_w.dict.yaml")

shutil.copyfile("./allfiles/terra_pinyin_onion_add.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./allfiles/terra_pinyin_onion.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/terra_pinyin_onion.dict.yaml")
shutil.copyfile("./allfiles/terra_pinyin_onion.extended.dict.yaml", "./sort_rime/地球拼音洋蔥mix-in版/terra_pinyin_onion.extended.dict.yaml")
shutil.copyfile("./allfiles/terra_pinyin_onion.schema.yaml", "./sort_rime/地球拼音洋蔥mix-in版/terra_pinyin_onion.schema.yaml")

shutil.copyfile("./allfiles/各方案default.custom/地球拼音洋蔥mix-in版_custom/default.custom.yaml", "./sort_rime/地球拼音洋蔥mix-in版/default.custom.yaml")

shutil.copyfile("./allfiles/opencc/back_mark_ocm.json", "./sort_rime/地球拼音洋蔥mix-in版/opencc/back_mark_ocm.json")
shutil.copyfile("./allfiles/opencc/back_mark_ocm.txt", "./sort_rime/地球拼音洋蔥mix-in版/opencc/back_mark_ocm.txt")


#複製檔案(ocm_mixin)
shutil.copyfile("./allfiles/essay-zh-hant-onion.txt", "./sort_rime/ocm/ocm_mixin/essay-zh-hant-onion.txt")
shutil.copyfile("./allfiles/allbpm.dict.yaml", "./sort_rime/ocm/ocm_mixin/allbpm.dict.yaml")
shutil.copyfile("./allfiles/allbpm.schema.yaml", "./sort_rime/ocm/ocm_mixin/allbpm.schema.yaml")
shutil.copyfile("./allfiles/cyrillic.dict.yaml", "./sort_rime/ocm/ocm_mixin/cyrillic.dict.yaml")
shutil.copyfile("./allfiles/cyrillic.extended.dict.yaml", "./sort_rime/ocm/ocm_mixin/cyrillic.extended.dict.yaml")
shutil.copyfile("./allfiles/easy_en_b.dict.yaml", "./sort_rime/ocm/ocm_mixin/easy_en_b.dict.yaml")
shutil.copyfile("./allfiles/easy_en_b.schema.yaml", "./sort_rime/ocm/ocm_mixin/easy_en_b.schema.yaml")
shutil.copyfile("./allfiles/easy_en_comment.dict.yaml", "./sort_rime/ocm/ocm_mixin/easy_en_comment.dict.yaml")
shutil.copyfile("./allfiles/easy_en_comment.schema.yaml", "./sort_rime/ocm/ocm_mixin/easy_en_comment.schema.yaml")
shutil.copyfile("./allfiles/fullshape.extended.dict.yaml", "./sort_rime/ocm/ocm_mixin/fullshape.extended.dict.yaml")
shutil.copyfile("./allfiles/fullshape.dict.yaml", "./sort_rime/ocm/ocm_mixin/fullshape.dict.yaml")
shutil.copyfile("./allfiles/greek.dict.yaml", "./sort_rime/ocm/ocm_mixin/greek.dict.yaml")
shutil.copyfile("./allfiles/greek.extended.dict.yaml", "./sort_rime/ocm/ocm_mixin/greek.extended.dict.yaml")
shutil.copyfile("./allfiles/Mount_bopomo.extended.dict.yaml", "./sort_rime/ocm/ocm_mixin/Mount_bopomo.extended.dict.yaml")
shutil.copyfile("./allfiles/Mount_bopomo.schema.yaml", "./sort_rime/ocm/ocm_mixin/Mount_bopomo.schema.yaml")
shutil.copyfile("./allfiles/Mount_ocm.extended.dict.yaml", "./sort_rime/ocm/ocm_mixin/Mount_ocm.extended.dict.yaml")
shutil.copyfile("./allfiles/Mount_ocm.schema.yaml", "./sort_rime/ocm/ocm_mixin/Mount_ocm.schema.yaml")

shutil.copyfile("./allfiles/ocm_mixin_cyrillic.schema.yaml", "./sort_rime/ocm/ocm_mixin/ocm_mixin_cyrillic.schema.yaml")
shutil.copyfile("./allfiles/ocm_mixin_fullshape.schema.yaml", "./sort_rime/ocm/ocm_mixin/ocm_mixin_fullshape.schema.yaml")
shutil.copyfile("./allfiles/ocm_mixin_greek.schema.yaml", "./sort_rime/ocm/ocm_mixin/ocm_mixin_greek.schema.yaml")
shutil.copyfile("./allfiles/ocm_mixin_jp.dict.yaml", "./sort_rime/ocm/ocm_mixin/ocm_mixin_jp.dict.yaml")
shutil.copyfile("./allfiles/ocm_mixin_kr.dict.yaml", "./sort_rime/ocm/ocm_mixin/ocm_mixin_kr.dict.yaml")
shutil.copyfile("./allfiles/ocm_mixin_la.dict.yaml", "./sort_rime/ocm/ocm_mixin/ocm_mixin_la.dict.yaml")
shutil.copyfile("./allfiles/ocm_mixin_phrase.txt", "./sort_rime/ocm/ocm_mixin/ocm_mixin_phrase.txt")
shutil.copyfile("./allfiles/ocm_mixin.extended.dict.yaml", "./sort_rime/ocm/ocm_mixin/ocm_mixin.extended.dict.yaml")
shutil.copyfile("./allfiles/ocm_mixin.schema.yaml", "./sort_rime/ocm/ocm_mixin/ocm_mixin.schema.yaml")

shutil.copyfile("./allfiles/punct_ovff.dict.yaml", "./sort_rime/ocm/ocm_mixin/punct_ovff.dict.yaml")
shutil.copyfile("./allfiles/punct_ovff.schema.yaml", "./sort_rime/ocm/ocm_mixin/punct_ovff.schema.yaml")
shutil.copyfile("./allfiles/symbols_ocm.dict.yaml", "./sort_rime/ocm/ocm_mixin/symbols_ocm.dict.yaml")
shutil.copyfile("./allfiles/symbols_ocm.schema.yaml", "./sort_rime/ocm/ocm_mixin/symbols_ocm.schema.yaml")

shutil.copyfile("./allfiles/terra_pinyin_onion_add.dict.yaml", "./sort_rime/ocm/ocm_mixin/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./allfiles/terra_pinyin_onion.dict.yaml", "./sort_rime/ocm/ocm_mixin/terra_pinyin_onion.dict.yaml")
shutil.copyfile("./allfiles/tcword.dict.yaml", "./sort_rime/ocm/ocm_mixin/tcword.dict.yaml")
shutil.copyfile("./allfiles/uniabcdword.dict.yaml", "./sort_rime/ocm/ocm_mixin/uniabcdword.dict.yaml")

shutil.copyfile("./allfiles/phrases.cht_en_w.dict.yaml", "./sort_rime/ocm/ocm_mixin/phrases.cht_en_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.cyr_all.dict.yaml", "./sort_rime/ocm/ocm_mixin/phrases.cyr_all.dict.yaml")
shutil.copyfile("./allfiles/phrases.en_l_w.dict.yaml", "./sort_rime/ocm/ocm_mixin/phrases.en_l_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.en_o_w.dict.yaml", "./sort_rime/ocm/ocm_mixin/phrases.en_o_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.en_u_w.dict.yaml", "./sort_rime/ocm/ocm_mixin/phrases.en_u_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.fs_all.dict.yaml", "./sort_rime/ocm/ocm_mixin/phrases.fs_all.dict.yaml")
shutil.copyfile("./allfiles/phrases.gr_all.dict.yaml", "./sort_rime/ocm/ocm_mixin/phrases.gr_all.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hk_more.dict.yaml", "./sort_rime/ocm/ocm_mixin/phrases.jp_hk_more.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hk.dict.yaml", "./sort_rime/ocm/ocm_mixin/phrases.jp_hk.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hkk.dict.yaml", "./sort_rime/ocm/ocm_mixin/phrases.jp_hkk.dict.yaml")
shutil.copyfile("./allfiles/phrases.kr_more.dict.yaml", "./sort_rime/ocm/ocm_mixin/phrases.kr_more.dict.yaml")
shutil.copyfile("./allfiles/phrases.kr.dict.yaml", "./sort_rime/ocm/ocm_mixin/phrases.kr.dict.yaml")
shutil.copyfile("./allfiles/phrases.la_py_w.dict.yaml", "./sort_rime/ocm/ocm_mixin/phrases.la_py_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.ocmtc_original.dict.yaml", "./sort_rime/ocm/ocm_mixin/phrases.ocmtc_original.dict.yaml")
shutil.copyfile("./allfiles/phrases.ocmtc_terra.dict.yaml", "./sort_rime/ocm/ocm_mixin/phrases.ocmtc_terra.dict.yaml")

shutil.copyfile("./allfiles/element_ocm.yaml", "./sort_rime/ocm/ocm_mixin/element_ocm.yaml")
shutil.copyfile("./allfiles/punct_ocm.yaml", "./sort_rime/ocm/ocm_mixin/punct_ocm.yaml")
shutil.copyfile("./allfiles/rime.lua", "./sort_rime/ocm/ocm_mixin/rime.lua")

shutil.copyfile("./allfiles/各方案default.custom/ocm_mixin_custom/default.custom.yaml", "./sort_rime/ocm/ocm_mixin/default.custom.yaml")

shutil.copyfile("./allfiles/opencc/back_mark_ocm.json", "./sort_rime/ocm/ocm_mixin/opencc/back_mark_ocm.json")
shutil.copyfile("./allfiles/opencc/back_mark_ocm.txt", "./sort_rime/ocm/ocm_mixin/opencc/back_mark_ocm.txt")
shutil.copyfile("./allfiles/opencc/emoji.json", "./sort_rime/ocm/ocm_mixin/opencc/emoji.json")
shutil.copyfile("./allfiles/opencc/emoji.txt", "./sort_rime/ocm/ocm_mixin/opencc/emoji.txt")
shutil.copyfile("./allfiles/opencc/ocm_big5e_hkscs_jis.json", "./sort_rime/ocm/ocm_mixin/opencc/ocm_big5e_hkscs_jis.json")
shutil.copyfile("./allfiles/opencc/ocm_big5e_hkscs_jis.txt", "./sort_rime/ocm/ocm_mixin/opencc/ocm_big5e_hkscs_jis.txt")
shutil.copyfile("./allfiles/opencc/punct_mark.json", "./sort_rime/ocm/ocm_mixin/opencc/punct_mark.json")
shutil.copyfile("./allfiles/opencc/punct_mark.txt", "./sort_rime/ocm/ocm_mixin/opencc/punct_mark.txt")


#複製檔案(ocm_plus)
shutil.copyfile("./allfiles/essay-zh-hant-onion.txt", "./sort_rime/ocm/ocm_plus/essay-zh-hant-onion.txt")
shutil.copyfile("./allfiles/allbpm.dict.yaml", "./sort_rime/ocm/ocm_plus/allbpm.dict.yaml")
shutil.copyfile("./allfiles/allbpm.schema.yaml", "./sort_rime/ocm/ocm_plus/allbpm.schema.yaml")
shutil.copyfile("./allfiles/cyrillic.dict.yaml", "./sort_rime/ocm/ocm_plus/cyrillic.dict.yaml")
shutil.copyfile("./allfiles/cyrillic.extended.dict.yaml", "./sort_rime/ocm/ocm_plus/cyrillic.extended.dict.yaml")
shutil.copyfile("./allfiles/easy_en_b.dict.yaml", "./sort_rime/ocm/ocm_plus/easy_en_b.dict.yaml")
shutil.copyfile("./allfiles/easy_en_b.schema.yaml", "./sort_rime/ocm/ocm_plus/easy_en_b.schema.yaml")
shutil.copyfile("./allfiles/easy_en_comment.dict.yaml", "./sort_rime/ocm/ocm_plus/easy_en_comment.dict.yaml")
shutil.copyfile("./allfiles/easy_en_comment.schema.yaml", "./sort_rime/ocm/ocm_plus/easy_en_comment.schema.yaml")
shutil.copyfile("./allfiles/fullshape.extended.dict.yaml", "./sort_rime/ocm/ocm_plus/fullshape.extended.dict.yaml")
shutil.copyfile("./allfiles/fullshape.dict.yaml", "./sort_rime/ocm/ocm_plus/fullshape.dict.yaml")
shutil.copyfile("./allfiles/greek.dict.yaml", "./sort_rime/ocm/ocm_plus/greek.dict.yaml")
shutil.copyfile("./allfiles/greek.extended.dict.yaml", "./sort_rime/ocm/ocm_plus/greek.extended.dict.yaml")
shutil.copyfile("./allfiles/Mount_bopomo.extended.dict.yaml", "./sort_rime/ocm/ocm_plus/Mount_bopomo.extended.dict.yaml")
shutil.copyfile("./allfiles/Mount_bopomo.schema.yaml", "./sort_rime/ocm/ocm_plus/Mount_bopomo.schema.yaml")
shutil.copyfile("./allfiles/ocm_mixin_jp.dict.yaml", "./sort_rime/ocm/ocm_plus/ocm_mixin_jp.dict.yaml")
shutil.copyfile("./allfiles/ocm_mixin_kr.dict.yaml", "./sort_rime/ocm/ocm_plus/ocm_mixin_kr.dict.yaml")
shutil.copyfile("./allfiles/ocm_mixin_la.dict.yaml", "./sort_rime/ocm/ocm_plus/ocm_mixin_la.dict.yaml")

shutil.copyfile("./allfiles/dif1_cy.schema.yaml", "./sort_rime/ocm/ocm_plus/dif1_cy.schema.yaml")
shutil.copyfile("./allfiles/dif1_fs.schema.yaml", "./sort_rime/ocm/ocm_plus/dif1_fs.schema.yaml")
shutil.copyfile("./allfiles/dif1_gr.schema.yaml", "./sort_rime/ocm/ocm_plus/dif1_gr.schema.yaml")
shutil.copyfile("./allfiles/dif1_jp.extended.dict.yaml", "./sort_rime/ocm/ocm_plus/dif1_jp.extended.dict.yaml")
shutil.copyfile("./allfiles/dif1_jphi.schema.yaml", "./sort_rime/ocm/ocm_plus/dif1_jphi.schema.yaml")
shutil.copyfile("./allfiles/dif1_jpka.schema.yaml", "./sort_rime/ocm/ocm_plus/dif1_jpka.schema.yaml")
shutil.copyfile("./allfiles/dif1_kr.extended.dict.yaml", "./sort_rime/ocm/ocm_plus/dif1_kr.extended.dict.yaml")
shutil.copyfile("./allfiles/dif1_kr.schema.yaml", "./sort_rime/ocm/ocm_plus/dif1_kr.schema.yaml")
shutil.copyfile("./allfiles/dif1_la.extended.dict.yaml", "./sort_rime/ocm/ocm_plus/dif1_la.extended.dict.yaml")
shutil.copyfile("./allfiles/dif1_la.schema.yaml", "./sort_rime/ocm/ocm_plus/dif1_la.schema.yaml")
shutil.copyfile("./allfiles/dif1_phrase.txt", "./sort_rime/ocm/ocm_plus/dif1_phrase.txt")
shutil.copyfile("./allfiles/dif1.extended.dict.yaml", "./sort_rime/ocm/ocm_plus/dif1.extended.dict.yaml")
shutil.copyfile("./allfiles/dif1.schema.yaml", "./sort_rime/ocm/ocm_plus/dif1.schema.yaml")

shutil.copyfile("./allfiles/phrases.cyr_all.dict.yaml", "./sort_rime/ocm/ocm_plus/phrases.cyr_all.dict.yaml")
shutil.copyfile("./allfiles/phrases.en_l_w.dict.yaml", "./sort_rime/ocm/ocm_plus/phrases.en_l_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.en_o_w.dict.yaml", "./sort_rime/ocm/ocm_plus/phrases.en_o_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.en_u_w.dict.yaml", "./sort_rime/ocm/ocm_plus/phrases.en_u_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.fs_all.dict.yaml", "./sort_rime/ocm/ocm_plus/phrases.fs_all.dict.yaml")
shutil.copyfile("./allfiles/phrases.gr_all.dict.yaml", "./sort_rime/ocm/ocm_plus/phrases.gr_all.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hk_more.dict.yaml", "./sort_rime/ocm/ocm_plus/phrases.jp_hk_more.dict.yaml")
shutil.copyfile("./allfiles/phrases.jp_hk.dict.yaml", "./sort_rime/ocm/ocm_plus/phrases.jp_hk.dict.yaml")
shutil.copyfile("./allfiles/phrases.kr.dict.yaml", "./sort_rime/ocm/ocm_plus/phrases.kr.dict.yaml")
shutil.copyfile("./allfiles/phrases.la_py_w.dict.yaml", "./sort_rime/ocm/ocm_plus/phrases.la_py_w.dict.yaml")
shutil.copyfile("./allfiles/phrases.ocmtc_original.dict.yaml", "./sort_rime/ocm/ocm_plus/phrases.ocmtc_original.dict.yaml")
shutil.copyfile("./allfiles/phrases.ocmtc_terra.dict.yaml", "./sort_rime/ocm/ocm_plus/phrases.ocmtc_terra.dict.yaml")

shutil.copyfile("./allfiles/punct_ovff.dict.yaml", "./sort_rime/ocm/ocm_plus/punct_ovff.dict.yaml")
shutil.copyfile("./allfiles/punct_ovff.schema.yaml", "./sort_rime/ocm/ocm_plus/punct_ovff.schema.yaml")
shutil.copyfile("./allfiles/symbols_ocm.dict.yaml", "./sort_rime/ocm/ocm_plus/symbols_ocm.dict.yaml")
shutil.copyfile("./allfiles/symbols_ocm.schema.yaml", "./sort_rime/ocm/ocm_plus/symbols_ocm.schema.yaml")

shutil.copyfile("./allfiles/terra_pinyin_onion_add.dict.yaml", "./sort_rime/ocm/ocm_plus/terra_pinyin_onion_add.dict.yaml")
shutil.copyfile("./allfiles/terra_pinyin_onion.dict.yaml", "./sort_rime/ocm/ocm_plus/terra_pinyin_onion.dict.yaml")
shutil.copyfile("./allfiles/tcword.dict.yaml", "./sort_rime/ocm/ocm_plus/tcword.dict.yaml")
shutil.copyfile("./allfiles/uniabcdword.dict.yaml", "./sort_rime/ocm/ocm_plus/uniabcdword.dict.yaml")

shutil.copyfile("./allfiles/element_ocm.yaml", "./sort_rime/ocm/ocm_plus/element_ocm.yaml")
shutil.copyfile("./allfiles/punct_ocm.yaml", "./sort_rime/ocm/ocm_plus/punct_ocm.yaml")
shutil.copyfile("./allfiles/rime.lua", "./sort_rime/ocm/ocm_plus/rime.lua")

shutil.copyfile("./allfiles/各方案default.custom/ocm_plus_custom/default.custom.yaml", "./sort_rime/ocm/ocm_plus/default.custom.yaml")

shutil.copyfile("./allfiles/opencc/back_mark.json", "./sort_rime/ocm/ocm_plus/opencc/back_mark.json")
shutil.copyfile("./allfiles/opencc/back_mark.txt", "./sort_rime/ocm/ocm_plus/opencc/back_mark.txt")
shutil.copyfile("./allfiles/opencc/emoji.json", "./sort_rime/ocm/ocm_plus/opencc/emoji.json")
shutil.copyfile("./allfiles/opencc/emoji.txt", "./sort_rime/ocm/ocm_plus/opencc/emoji.txt")
shutil.copyfile("./allfiles/opencc/ocm_big5e_hkscs_jis.json", "./sort_rime/ocm/ocm_plus/opencc/ocm_big5e_hkscs_jis.json")
shutil.copyfile("./allfiles/opencc/ocm_big5e_hkscs_jis.txt", "./sort_rime/ocm/ocm_plus/opencc/ocm_big5e_hkscs_jis.txt")
shutil.copyfile("./allfiles/opencc/punct_mark.json", "./sort_rime/ocm/ocm_plus/opencc/punct_mark.json")
shutil.copyfile("./allfiles/opencc/punct_mark.txt", "./sort_rime/ocm/ocm_plus/opencc/punct_mark.txt")


#其他
shutil.copytree('./allfiles/其他/', './sort_rime/其他/')

shutil.copytree('./allfiles/其他/OpenCC_ocd_64位元/', './sort_rime/ocm/OpenCC_ocd_64位元/')
shutil.copytree('./allfiles/ocm_防崩潰：Win必加，Mac勿加/', './sort_rime/ocm/ocm_防崩潰：Win必加，Mac勿加/')


#主程式
shutil.copytree('./allfiles/主程式/', './sort_rime/主程式/')


#增加日期
localtime=time.strftime("%Y%m%d", time.localtime())

os.rename('./sort_rime/地球拼音洋蔥mix-in版/', './sort_rime/地球拼音洋蔥mix-in版_'+localtime)
os.rename('./sort_rime/注音洋蔥純注音版/', './sort_rime/注音洋蔥純注音版_'+localtime)
os.rename('./sort_rime/注音洋蔥雙拼版/', './sort_rime/注音洋蔥雙拼版_'+localtime)
os.rename('./sort_rime/注音洋蔥mixin版/', './sort_rime/注音洋蔥mixin版_'+localtime)
os.rename('./sort_rime/注音洋蔥plus版/', './sort_rime/注音洋蔥plus版_'+localtime)

os.rename('./sort_rime/ocm/ocm_mixin/', './sort_rime/ocm/ocm_mixin_'+localtime)
os.rename('./sort_rime/ocm/ocm_plus/', './sort_rime/ocm/ocm_plus_'+localtime)
os.rename('./sort_rime/ocm/', './sort_rime/ocm_'+localtime)

os.rename('./sort_rime/', './電腦RIME方案_'+localtime)


