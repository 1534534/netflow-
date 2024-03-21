<template>
  <div>
    <!--页面区域-->
    <a id="resource" style="width: 100vw;height: 40vh;left: -100px;"></a>
    <tbody>
      <a :key="allData">{{ allData.uploadAll }}</a>

      <tr>
        <td class="el-table__cell is-leaf">
          <div class="cell">累计上传:</div>
        </td>
        <td class="el-table__cell is-leaf">
          <div class="cell" v-if="allData.uploadAll">{{ allData.uploadAll }}%</div>
        </td>
      </tr>
      <tr>
        <td class="el-table__cell is-leaf">
          <div class="cell">累计下载:</div>
        </td>
        <td class="el-table__cell is-leaf">
          <div class="cell" v-if="allData.downloadAll">{{ allData.downloadAll }}%</div>
        </td>
      </tr>
      <tr>
        <td class="el-table__cell is-leaf">
          <div class="cell">CPU利用率:</div>
        </td>
        <td class="el-table__cell is-leaf">
          <div class="cell" v-if="allData.cpu_used">{{ allData.cpu_used }}%</div>
        </td>
      </tr>
    </tbody>
  </div>
</template>
<script setup lang="ts">
import { ref, reactive } from "vue"
import { createApi, listApi, updateApi, deleteApi } from '/@/api/thing';
// 引入 echarts 核心模块，核心模块提供了 echarts 使用必须要的接口。
import * as echarts from "echarts/core";
// 引入柱状图and折线图图表，就是图表后面的内容，以Chart结尾（下面放有图片）
import {
  BarChart,
  LineChart,
  PieChart
} from "echarts/charts";
// 引入提示框，标题，直角坐标系，数据集，内置数据转换器组件，组件后缀都为 Component
import {
  TitleComponent,
  TooltipComponent,
  GridComponent,
  DatasetComponent,
  TransformComponent,
  ToolboxComponent,
  LegendComponent
} from "echarts/components";
// 标签自动布局，全局过渡动画等特性
import {
  LabelLayout,
  UniversalTransition
} from "echarts/features";
// 引入 Canvas 渲染器，注意引入 CanvasRenderer 或者 SVGRenderer 是必须的一步
import {
  CanvasRenderer
} from "echarts/renderers";
// 注册必须的组件
echarts.use([
  TitleComponent,
  TooltipComponent,
  GridComponent,
  DatasetComponent,
  TransformComponent,
  BarChart,
  LabelLayout,
  UniversalTransition,
  CanvasRenderer,
  LineChart,
  PieChart,
  ToolboxComponent,
  LegendComponent
]);
// 页面数据
const data = reactive({
  dataList: [],
  loading: false,
  keyword: '',
  selectedRowKeys: [] as any[],
  pageSize: 10,
  page: 1,
});
onMounted(() => {
  getDataList();
});
const timer = ref(); // 定时器
//循环请求接口
const meterTimeFn = () => {
  timer.value = setInterval(() => {
    getDataList();// 请求数据 
    clearInterval(timer.value);
    timer.value = null;

  }, 1000);
};
let uploadSpeed = []
let downloadSpeed = []
let allData = reactive({
  uploadAll: '',
  downloadAll: '',
  cpu_used: '',
})
let time = []
const getDataList = () => {
  data.loading = true;
  listApi({
    keyword: data.keyword,
  })
    .then((res) => {

      data.loading = false;
      res.data.forEach((item: any, index: any) => {
        item.index = index + 1;
      });
      data.dataList = res.data;
      data.dataList.forEach((item: any, index: any) => {
        uploadSpeed.push(item[1].slice(0, -4))
        downloadSpeed.push(item[2].slice(0, -5))
        allData.uploadAll = item[3]
        allData.downloadAll = item[4]

        time.push(item[5].slice(-8,))
        allData.cpu_used = item[6]

        if (uploadSpeed.length > 20) {
          uploadSpeed.shift()
        }
        if (downloadSpeed.length > 20) {
          downloadSpeed.shift()
        }
        if (time.length > 20) {
          time.shift()
        }
        drawDemo()
      })
      meterTimeFn()
    })
    .catch((err) => {
      data.loading = false;
      console.log(err);
    });
}
const drawDemo = () => {
  let myChart = echarts.init(document.getElementById('resource'));
  var option;
  var colors = ['#5470C6', '#EE6666'];
  option = {
    color: colors,
    tooltip: {
      trigger: 'none',
      axisPointer: {
        type: 'cross'
      }
    },
    legend: {
      data: ['下载速率', '上传速率']
    },
    grid: {
      top: 70,
      bottom: 50
    },
    xAxis: [{
      type: 'category',
      axisTick: {
        alignWithLabel: true
      },
      axisLine: {
        onZero: false,
        lineStyle: {
          color: colors[1]
        }
      },
      axisPointer: {
        label: {
          formatter: function (params) {
            return '下载速率  ' + params.value +
              (params.seriesData.length ? '：' + params.seriesData[0].data : '');
          }
        }
      },
      data: time
    },
    {
      type: 'category',
      axisTick: {
        alignWithLabel: true
      },
      axisLine: {
        onZero: false,
        lineStyle: {
          color: colors[0]
        }
      },
      axisPointer: {
        label: {
          formatter: function (params) {
            return '上传速率  ' + params.value +
              (params.seriesData.length ? '：' + params.seriesData[0].data : '');
          }
        }
      },

    }
    ],
    yAxis: [{
      type: 'value'
    }],
    series: [{
      name: '下载速率',
      type: 'line',
      xAxisIndex: 1,
      smooth: true,
      emphasis: {
        focus: 'series'
      },
      data: downloadSpeed
    },
    {
      name: '上传速率',
      type: 'line',
      smooth: true,
      emphasis: {
        focus: 'series'
      },
      data: uploadSpeed
    }
    ]
  };

  option && myChart.setOption(option);
}
</script>

<style scoped lang="less">
.content {
  width: 100vw;
  height: 50vh;
  padding: 0px;

}
</style>
