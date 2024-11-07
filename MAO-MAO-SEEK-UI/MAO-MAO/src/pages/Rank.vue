<template>
  <v-app>
    <v-container :style="{ maxWidth: '1000px' }" fluid>
      <!-- 头部导航栏 -->
      <!-- 使用HeadBar组件 -->
      <HeadBar/>
      <v-main>
        <v-card
          flat
          title="搜索"
        >
          <template v-slot:text>
            <v-text-field
              v-model="search"
              hide-details
              label="Search"
              prepend-inner-icon="mdi-magnify"
              single-line
              variant="outlined"
            ></v-text-field>
          </template>

          <v-data-table
            :headers="headers"
            :items="desserts"
            :search="search"
          >
            <template #item.login="{item}">
              <v-btn @click="navigateToProfile(item.login)">
                {{ item.login }}
              </v-btn>
            </template>
          </v-data-table>
        </v-card>
      </v-main>
      <!-- 网站页脚 -->
      <FooterBar/>
    </v-container>
  </v-app>
</template>

<script lang="ts" setup>
import {ref} from 'vue'
import {desserts, headers, navigateToProfile} from '@/public/github_rank_China'
// 搜索输入
const search = ref<string>('')
</script>


