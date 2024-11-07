<!--
 * @Author: jiang
 * @Date: 2024-11-05 22:34:35
 * @LastEditors: jiang
 * @LastEditTime: 2024-11-06 22:13:50
 * @FilePath: \MAO-MAO-SEEK-UI\MAO-MAO\src\components\HeadBar.vue
 * @Description:
 *
 * Copyright (c) 2024 by jiang, All Rights Reserved.
-->
<template>
  <!-- 头部导航栏 -->
  <v-card>
    <v-toolbar color="white">
      <!-- 应用栏 -->
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
      <v-toolbar-title>MAO-MAO</v-toolbar-title>
      <v-spacer></v-spacer>
      <!-- <v-btn elevation="5">登录</v-btn> -->
      <!-- 登录对话框 -->
      <Login/>
      <!-- 选项卡 -->
      <template v-slot:extension>
        <v-tabs v-model="activeTab" align-tabs="title" center-active>
          <v-tab v-for="tab in tabs" :key="tab.id" :to="tab.href">
            {{ tab.name }}
          </v-tab>
        </v-tabs>
      </template>
    </v-toolbar>
  </v-card>
  <v-spacer class="my-6"></v-spacer>
</template>

<script lang="ts" setup>
import {ref} from 'vue';
import Login from "@/components/Login.vue";
import {tabs} from '@/public/public'
// 活动的 Tab 索引
const activeTab = ref(0); // 这里使用 `v-model` 来绑定当前活动的 Tab
</script>
