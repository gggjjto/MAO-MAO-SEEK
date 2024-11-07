<!--
 * @Author: jiang
 * @Date: 2024-11-05 15:34:09
 * @LastEditors: jiang
 * @LastEditTime: 2024-11-06 17:26:34
 * @FilePath: \MAO-MAO-SEEK-UI\MAO-MAO\src\pages\index.vue
 * @Description:
 *
 * Copyright (c) 2024 by jiang, All Rights Reserved.
-->

<template>
  <v-app>
    <v-container :style="{ maxWidth: '1000px' }" fluid>
      <!-- 头部导航栏 -->
      <!-- 使用HeadBar组件 -->
      <HeadBar/>
      <!-- 视差图背景 -->
      <v-main>
        <v-parallax :src="src">
          <div class="d-flex flex-column fill-height justify-center align-center text-white">
            <h1 class="text-h4 font-weight-thin mb-4">
              MAO-MAO
            </h1>
            <h4 class="subheading">
              GitHub 数据应用
            </h4>
          </div>
        </v-parallax>
      </v-main>
      <!-- 主页卡片 -->
      <v-container fluid>
        <v-row class="d-flex justify-center ">
          <v-col cols="auto">
            <v-card :to="tabs[1].href" max-width="200px">
              <v-card-title>查询</v-card-title>
              <v-card-subtitle>开发者共建代码世界</v-card-subtitle>
            </v-card>
          </v-col>
          <v-spacer></v-spacer>
          <v-col cols="auto">
            <v-card :to="tabs[2].href" max-width="200px">
              <v-card-title>排名</v-card-title>
              <v-card-subtitle>观摩大佬之华山论剑</v-card-subtitle>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
      <!-- 网站页脚 -->
      <FooterBar/>
    </v-container>
  </v-app>
</template>

<script lang="ts" setup>
import {src, tabs} from '@/public/public'
</script>
