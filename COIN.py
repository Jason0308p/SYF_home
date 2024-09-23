/**
* 对返回的数据做一些自定义处理
* 返回数据文档：https://www.yuque.com/yida/support/xgg4ps
* data: 返回的数据
* extraInfo: { meta: [], cardParams: {} }，meta 代表数据元信息，cardParams 代表卡片参数信息
*/
function afterFetch(data, extraInfo) {
  let $rate = [{ name: "人民幣", sort: 0, rate: 4.50 }, { name: "美元", sort: 1, rate: 32.40 }, { name: "新台幣", sort: 2, rate: 1 }, { name: "港幣", sort: 3, rate: 4.20 }]

  let arr = []
  data.forEach(item => {
    let $x = 1
    //console.log($x)
    switch (item.field_luc4hai5) {
      case "人民幣":
        $x = $rate[0].rate
        break;
      case "美元":
        $x = $rate[1].rate
        break;
      case "新台幣":
        $x = $rate[2].rate
        break;
      case "港幣":
        $x = $rate[3].rate
        break;
    }

    item.field_luc4hak1 = (item.field_luc4hai3 * $x).toFixed(0);
    item.field_luc4hak3 = (item.field_luc4hak1 * 2.2).toFixed(0);
    //item.field_lth399af = (item.field_ltgybycb * $x).toFixed(0) + "-" + "$" + (item.field_ltgybyc9 * $x).toFixed(0)
    //console.log(item.field_ltscpdh6)
    //console.log(item.field_lth399af)
    let $x2 = 0
    switch (item.field_luc4haiv) {
      case "人民幣":
        $x2 = $rate[0].rate
        break;
      case "美元":
        $x2 = $rate[1].rate
        break;
      case "新台幣":
        $x2 = $rate[2].rate
        break;
      case "港幣":
        $x2 = $rate[3].rate
        break;
    }
    if (item.field_luc4hajx) {
      let str = item.field_luc4hajx
      let newArray = str.split("-").map(x => (x * $x2).toFixed(0))

      item.field_luc4hajz ="$"+newArray.join("-")
      //console.log(cost)
    }

    item.field_lugv5e31 = item.field_luc4hai1 * item.field_luc4hak3

    arr.push(item)
  })
  data = arr
  return data;
}
