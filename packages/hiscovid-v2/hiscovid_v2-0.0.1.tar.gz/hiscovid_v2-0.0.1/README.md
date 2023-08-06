# hiscovid_v2


hiscovid_v2の目的は政策提案者の失敗を特定することです。

hiscovid_v2はcovid-19による各国の死者数の総計をその国の人口で割ったスコアを時系列でグラフにし、そのスコアのグラフの傾きを示したものです。

そのスコアのグラフは連続値で単調増加関数です。そのため、急激にグラフが増加しているところで政策提案者が間違いを犯していることとなります。

したがって、このグラフの微分(傾き)を取れば、政策提案者の間違いをより明確に表すことができると考えました。

グラフの値が高いところほど、政策提案者はより深刻な間違いを犯していると考えることができます。

hiscovid_v2 は、インターネットを介して次のサイトから最新のデータをスクレイピングします。

https://covid.ourworldindata.org/data/owid-covid-data.csv



# hiscovid_v2のインストール方法
$pip install hiscovid_v2

# hiscovid_v2の実行方法
h iscovid_v2 <国名>

$ hiscovid_v2 Japan "South Korea"

<img src="japan_southkorea.png" width="400">

$ hiscovid_v2 Japan Taiwan

<img src="japan_taiwan.png" width="400">

<!--
$ hiscovid_v2 Taiwan 'New Zealand'
<img src="taiwan_newzealand.png" width="400">
-->
$ hiscovid_v2 Taiwan 'United States' 'United Kingdom'

<img src="taiwan_unitedstates_unitedkingdom.png" width="400">


