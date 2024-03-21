<template>
  <div class="page-view">
    <a-spin v-bind:spinning="loading">
      <a-descriptions title="系统信息" bordered :column="{ lg: 2, md: 2, sm: 1 }">
        <a-descriptions-item label="操作系统">
          {{ data.osName }}
        </a-descriptions-item>
        <a-descriptions-item label="系统平台">
          {{ data.pf }}
        </a-descriptions-item>
        <a-descriptions-item label="CPU核数">
          {{ data.cpuCount }}
        </a-descriptions-item>
        <a-descriptions-item label="处理器">
          {{ data.processor }}
        </a-descriptions-item>
        <a-descriptions-item label="系统内存">
          {{ data.memory }}G
        </a-descriptions-item>
        <a-descriptions-item label="内存使用">
          {{ data.usedMemory }}G
        </a-descriptions-item>
        <a-descriptions-item label="内存利用率">
          {{ data.percentMemory }}%
        </a-descriptions-item>
        <a-descriptions-item label="本次开机时间">
          {{ data.start_time }}
        </a-descriptions-item>
        <a-descriptions-item label="C盘内存使用率">
          {{ data.use_percent_C }}%
        </a-descriptions-item>
        <a-descriptions-item label="D盘内存使用率">
          {{ data.use_percent_D }}%
        </a-descriptions-item>
      </a-descriptions>
    </a-spin>
  </div>
</template>
<script>
import { sysInfoApi } from '/@/api/sysInfo'

export default {
  data() {
    return {
      loading: false,
      data: {},
    }
  },
  methods: {
    getSysInfo() {
      this.loading = true
      sysInfoApi().then(res => {
        this.loading = false
        this.data = res.data
        console.log(this.data);
      })
    }
  },
  mounted() {
    this.getSysInfo()
  }
}
</script>

<style lang="less" scoped>
.table-wrap {
  flex: 1;
}

.page-view {
  min-height: 100%;
  background: #FFF;
  padding: 24px;
  display: flex;
  flex-direction: column;
}

.table-operation {
  height: 50px;
  text-align: right;
}
</style>
