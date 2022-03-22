# Onion_Rime_Files：電腦 Rime（注音、雙拼、拼音、形碼、行列30）洋蔥方案

####  ※ 請勿使用於商業營利相關行為
####  ※ Commercial use is prohibited

### 內容說明：
- allfiles 中包含九個主方案（三個注音、一個注音雙拼、一個拼音、三個形碼、一個行列30）和一眾掛接方案

- 三個形碼方案無法使用，因已刪除碼表內容！

- 掛接方案包含：拉丁字母（含音標）、希臘字母、西里爾（俄）字母、全形數字字母、Easy 英文（含註釋字典）、日文（含漢字）、兩個韓文（HNC和形碼，含單音含漢字）、 注音文、Emoji 顏文字符號系列集等。

- allfiles 中的檔案不直接一個資料夾一個方案，因較好更新，不用同一個檔案更新數次。

- 提供 Python (sort_rime_file.py) 文件，把 Rime 文件分門別類到各個方案資料夾，使其易安裝部署

### sort_rime_file.py 使用方法：
- 於本倉庫 Onion_Rime_Files 中按右上綠色 〔↓Code〕 ⇨ Download ZIP ⇨ 解壓縮 ZIP ⇨ 進入解壓縮後的資料夾，確認 allfiles 資料夾 和 sort_rime_file.py 是在同一層 ⇨ 執行 sort_rime_file.py ⇨ 產生一個『電腦RIME方案_{當天日期}』資料夾

- 產生的『電腦RIME方案_{當天日期}』該資料夾內，會把各方案所須文件，分別在該『方案名稱』資料夾內。

- 選取想要的方案，把內含文件通通放入『 Rime 』用戶設定資料夾，如已有 opencc 資料夾，移動 opencc 裡面檔案到 opencc 資料夾內，沒有的話，整個 opencc 移過去，按「重新部署」即可使用。

```
~/Library/Rime  ( Mac OS 鼠鬚管 )
%APPDATA%\Rime  ( Windows 小狼毫 )
~/.config/ibus/rime  ( Linux 中州韻 )
~/.config/fcitx/rime  ( Linux )

不要放錯資料夾，上方為正確路徑。
反饋有好幾人放錯放到程式本身攜帶方案之預設資料夾 orz ！雖可使用，但某些功能會有問題。
Linux 上反饋問題很多，一看其 Rime 核心 librime 過舊，librime-lua 掛件也缺失，使用前請注意！並自行解決！
裡面所有方案皆以 Mac 鼠鬚管官方最新封裝版本為實作基礎。
使用 Windows 小狼毫官方最新封裝版本，如使用方案內有 rime.lua 該檔，建議更換最新官方封裝 librime 核心！
因早期 librime-lua 版本使用遍尋時會產生記憶體洩漏，更新版已解決。
```

  > 《 Windows 用戶注意！！！》，注音（洋蔥 plus 版）和注音（洋蔥 mix‧in 版）掛接《Easy》，使用提示碼做英漢字典，但 Windows 輸入時，整頁提示碼太多會使程式崩潰！故以正則簡化提示碼！不過 Windows 可行程式碼在 Mac 會使《Easy》無法正常出字！提供 custom 檔給 Windows 用戶，防止程式崩潰（ Mac 用戶勿使用該 custom 檔）。分別在「plus注音_防崩潰：Win必加，Mac勿加」和「mixin注音_同顯2修改檔(Win)」資料夾內，Windows 用戶把資料夾內 custom.yaml 檔拖到上一層（和方案中其他文件同一層），按「重新部署」即可。

  > 如果缺少檔案，會立即出錯無法執行！
  
  > 用 Visual Studio Code 等非 Python 原生程式執行 sort_rime_file.py 會出錯（需另設定），使用 Python 原生程式執行即可。

### 各方案說明：

> 密碼：onionrime，請勿傳播密碼！

> 202203 韓文改成 HNC 羅馬字輸入方式。

- [電腦 RIME 輸入法『注音（洋蔥 純注音 版）』](https://deltazone.pixnet.net/blog/post/264319309)

- [電腦 RIME 輸入法『注音（洋蔥 plus 版）』](https://deltazone.pixnet.net/blog/post/343650692)

- [電腦 RIME 輸入法『注音（洋蔥 mix‧in 版）』](https://deltazone.pixnet.net/blog/post/347368709)

- [電腦 RIME 輸入法『注音（洋蔥 雙拼 版）』](https://deltazone.pixnet.net/blog/post/359775341)

- [電腦 RIME 輸入法〖 地球拼音（洋蔥 mix‧in 版）〗](https://deltazone.pixnet.net/blog/post/353697089)

- [電腦 RIME 設定檔〖 行列 30（洋蔥版）〗](https://deltazone.pixnet.net/blog/post/361766142)


### Demo：

- 注音（洋蔥 mix-in 版）
  
  > 集大成，多國語言和注音混打輸入 😃！
  
  #### ![image](https://raw.githubusercontent.com/oniondelta/Onion_Rime_Files/master/img/demo_bpmf_mixin.gif)
  
- 注音（洋蔥 plus 版）

  > 功能多，除外語還有一堆功能和細節增加，輸入手感和純注音版一樣，即使沒用外語，也推薦使用！
  
  #### ![image](https://raw.githubusercontent.com/oniondelta/Onion_Rime_Files/master/img/demo_bpmf_plus.gif)
  
- 注音（洋蔥 純注音 版）
  
  > 精簡功能，給新手或測試使用
  
  #### ![image](https://raw.githubusercontent.com/oniondelta/Onion_Rime_Files/master/img/demo_bpmf_pure.gif)
 
### Keys：
 
- 注音（洋蔥 雙拼 版）鍵位
  > 無加 custom 可簡拼，有 custom 為一般雙拼每字須鍵兩碼（聲調可省略）

  #### ![image](https://raw.githubusercontent.com/oniondelta/Onion_Rime_Files/master/allfiles/%E9%9B%99%E6%8B%BC%E6%B3%A8%E9%9F%B3%E9%8D%B5%E4%BD%8D%E8%AA%AA%E6%98%8E%E5%9C%96%E7%A4%BA/%E6%B3%A8%E9%9F%B3%E6%B4%8B%E8%94%A5%E9%9B%99%E6%8B%BC%E8%AA%AA%E6%98%8E.png)

- 注音（洋蔥 plus 版）鍵位

  #### ![image](https://raw.githubusercontent.com/oniondelta/Onion_Rime_Files/master/img/bpmf_plus_keyboard.png)

- 注音（洋蔥 mixin 版）鍵位

  > 四個衍伸方案：「1」標準版、「2」只有後綴易懂、「3」語言分野最明減少撞碼、「4」集中下排手順最好

  #### ![image](https://raw.githubusercontent.com/oniondelta/Onion_Rime_Files/master/img/bpmf_mixin_1_keyboard.png)
  
  
  #### ![image](https://raw.githubusercontent.com/oniondelta/Onion_Rime_Files/master/img/bpmf_mixin_2_keyboard.png)
  
  
  #### ![image](https://raw.githubusercontent.com/oniondelta/Onion_Rime_Files/master/img/bpmf_mixin_3_keyboard.png)
  
  
  #### ![image](https://raw.githubusercontent.com/oniondelta/Onion_Rime_Files/master/img/bpmf_mixin_4_keyboard.png)
  
- 注音洋蔥版選字鍵位

  #### ![image](https://raw.githubusercontent.com/oniondelta/Onion_Rime_Files/master/img/bpmf_select_keys_keyboard.png)

### 贊助 Donate：

  > 從第一個方案上傳已持續更新四年！方案從頭到尾大改、新創、新增非常多功能！且做了許多圖文說明！花了族繁不及備載的心力！

  > 懇請贊助 (Donate) 支持，讓 Rime 洋蔥的一系列方案更新更有動力！

- [按此以〈綠界〉贊助 Donate：](https://p.ecpay.com.tw/D555162)

  #### [![donate1](https://payment.ecpay.com.tw/Upload/QRCode/202010/QRCode_170c287e-2db8-4b50-b87f-8d36500a3958.png)](https://p.ecpay.com.tw/D555162)

- [按此以〈歐付寶〉贊助 Donate：](https://qr.opay.tw/q1ql7)

  #### [![donate2](https://payment.opay.tw/Upload/Broadcaster/2294343/QRcode/QRCode_7AC0FA1CAD39F0B66CFD5513A2173D1A.png)](https://qr.opay.tw/q1ql7)

