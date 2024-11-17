<template>
  <v-app>
    <v-container :style="{ maxWidth: '1000px' }" fluid>
      <!-- 头部导航栏 -->
      <!-- 使用HeadBar组件 -->
      <HeadBar/>
      <v-card>
        <v-tabs
          v-model="tab"
          bg-color="primary"
        >
          <v-tab value="one">中国开发者</v-tab>
          <v-tab value="two">美国开发者</v-tab>
        </v-tabs>
        <v-card-text>
          <v-tabs-window v-model="tab">
            <v-tabs-window-item value="one">
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
            </v-tabs-window-item>
            <v-tabs-window-item value="two">
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
                    :headers="USA_headers"
                    :items="USA_desserts"
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
            </v-tabs-window-item>
          </v-tabs-window>
        </v-card-text>
      </v-card>
      <!-- 网站页脚 -->
      <FooterBar/>
    </v-container>
  </v-app>
</template>

<script lang="ts" setup>
import {ref} from 'vue'
import {desserts, headers, navigateToProfile} from '@/public/github_rank_China'
import {USA_desserts, USA_headers} from "@/public/github_rank_USA";
import HeadBar from "@/components/HeadBar.vue";
// 搜索输入
const search = ref<string>('')
const tab = ref("one")
</script>


