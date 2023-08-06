# jpcovid

jpcovidの目的は日本の都道府県ごとのcovid-19に対する政策の政策提案者の失敗を特定することです。

jpcovidはcovid-19による都道府県ごとの死者数の総計をその都道府県の人口で割ったスコアを時系列でグラフにしました

そのスコアのグラフは連続値で単調増加関数です。そのため、急激にグラフが増加しているところで政策提案者が間違いを犯していることとなります。

グラフの値が高いところほど、政策提案者はより深刻な間違いを犯していると考えることができます。

jpcovid は、インターネットを介して次のサイトから最新のデータをスクレイピングします。

https://www3.nhk.or.jp/n-data/opendata/coronavirus/nhk_news_covid19_prefectures_daily_data.csv


# jpcovidのインストール方法
$pip install jpcovid

# jpcovidの実行方法
$ jpcovid <都道府県名>

$ jpcovid Tokyo Osaka

<img src="tokyo_osaka.png" width="400">

$ jpcovid Tokyo Tottori

<img src="tokyo_tottori.png" width="400">

$ jpcovid Osaka Niigata

<img src="osaka_niigata.png" width="400">

$ jpcovid Hokkaido Nara

<img src="hokkaido_nara.png" width="400">
