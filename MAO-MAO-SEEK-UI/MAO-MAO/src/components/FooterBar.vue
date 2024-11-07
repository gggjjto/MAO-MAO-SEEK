<!--
 * @Author: jiang
 * @Date: 2024-11-05 22:46:41
 * @LastEditors: jiang
 * @LastEditTime: 2024-11-05 22:46:56
 * @FilePath: \MAO-MAO-SEEK-UI\MAO-MAO\src\components\FooterBar.vue
 * @Description:
 *
 * Copyright (c) 2024 by jiang, All Rights Reserved.
-->
<template>
  <v-footer style="margin-top: 50px;">
    <div class="white text-center d-flex flex-column">
      <v-btn v-for="icon in icons" :key="icon.id" :href="icon.src" :icon="icon.icon" class="mx-4" location="center"
             variant="text"></v-btn>
      <div class="pt-0 text-center">
        这是参加1024创造节校园编程马拉松的一份编程作品，七天牛让这一切都很有趣，为热爱编程的开发者们进行一次有趣的数据分析。
      </div>
      <v-divider></v-divider>
      <div class="text-center">
        {{ new Date().getFullYear() }} —— <strong>Gggjjto</strong>
      </div>
    </div>
  </v-footer>
</template>

<script lang="ts" setup>
import {icons} from '@/public/public'
</script>
