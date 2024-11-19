<template>
  <v-app>
    <v-container :style="{ maxWidth: '1000px' }" fluid>
      <!-- 头部导航栏 -->
      <!-- 使用HeadBar组件 -->
      <HeadBar/>
      <!-- 视差图背景 -->
      <v-parallax :src="src">
        <v-spacer class="my-6"></v-spacer>
        <!-- 搜索栏 -->
        <v-main>
          <v-card
            class="mx-auto"
            color="surface-light"
            max-width="400"
          >
            <v-card-text>
              <v-text-field
                v-model="username"
                :loading="loading"
                append-inner-icon="mdi-magnify"
                density="compact"
                hide-details
                label="请搜索您喜欢的用户login"
                single-line
                variant="solo"
                @click:append-inner="onClick"
              ></v-text-field>
            </v-card-text>
          </v-card>
        </v-main>
        <v-spacer class="my-6"></v-spacer>
        <!-- 错误框 -->
        <v-slide-y-transition>
          <v-main v-if="error" class="d-flex justify-center align-center" width="100%">
            <v-alert class="text-center" close-icon="" dismissible style="max-width: 500px;" type="error"
                     @click="onErrorDismissed">{{ error }}
            </v-alert>
          </v-main>
        </v-slide-y-transition>
        <v-main v-if="loaded">
          <v-spacer class="my-6"></v-spacer>
          <v-main class="d-flex justify-center align-center">
            <v-card color="grey-lighten-5" elevation="16" height="30vw" hover width="40vw">
              <!-- 开发者头像 -->
              <v-card-title class="d-flex justify-center align-center">
                <v-avatar class="me-2" size="60">
                  <img :src="avatarUrl" alt="User Avatar" class="avatar-img"/>
                </v-avatar>
              </v-card-title>
              <!-- 用户名 -->
              <v-card-subtitle class="d-flex justify-center align-center black font-weight-bold">
                <v-row>
                  <v-col class="text-center" cols="4">
                    <v-chip class="ma-2" color="primary" label>
                      <v-icon icon="mdi-account-circle" start></v-icon>
                      {{ Login }}
                    </v-chip>
                  </v-col>
                  <v-col class="text-center" cols="4">
                    <v-chip class="ma-2" color="primary" label>
                      <v-icon icon="mdi-flag" start></v-icon>
                      {{ user?.country }}
                    </v-chip>
                  </v-col>
                  <v-col class="text-center" cols="4">
                    <v-chip class="ma-2" color="primary" label>
                      <v-icon icon="mdi-flag" start></v-icon>
                      可信度: {{ user?.reliability }}
                    </v-chip>
                  </v-col>
                </v-row>
              </v-card-subtitle>

              <!-- 用户信息内容 -->
              <v-card-text>
                <!-- 部分用户信息 -->
                <v-row>
                  <!-- 粉丝 -->
                  <v-col class="text-center" cols="4">
                    <v-chip color="orange lighten-3">
                      <v-icon class="me-2" color="primary">mdi-account-group</v-icon>
                      <span>粉丝: {{ user?.followers }}</span>
                    </v-chip>
                  </v-col>

                  <!-- 关注 -->
                  <v-col class="text-center" cols="4">
                    <v-chip color="pink lighten-3">
                      <v-icon class="me-2" color="primary">mdi-account-multiple</v-icon>
                      <span>关注: {{ user?.following }}</span>
                    </v-chip>
                  </v-col>

                  <!-- 仓库数量 -->
                  <v-col class="text-center" cols="4">
                    <v-chip color="purple lighten-3">
                      <v-icon class="me-2" color="primary">mdi-book-open-page-variant</v-icon>
                      <span>仓库: {{ user?.repos }}</span>
                    </v-chip>
                  </v-col>

                  <!-- 公司信息 -->
                  <v-col class="text-center" cols="4">
                    <v-chip color="blue lighten-3">
                      <v-icon class="me-2" color="primary">mdi-office-building</v-icon>
                      <span>公司: {{ user?.company || '未提供' }}</span>
                    </v-chip>
                  </v-col>


                  <!-- 位置 -->
                  <v-col class="text-center" cols="4">
                    <v-chip color="green lighten-3">
                      <v-icon class="me-2" color="primary">mdi-map-marker</v-icon>
                      <span>位置: {{ user?.location || '未提供' }}</span>
                    </v-chip>
                  </v-col>

                  <!-- 评分 -->
                  <v-col class="text-center" cols="4">
                    <v-chip color="teal lighten-3">
                      <v-icon class="me-2" color="primary">mdi-information-outline</v-icon>
                      <span>评分: {{ user?.score || '未提供' }}</span>
                    </v-chip>
                  </v-col>
                </v-row>
                <v-spacer class="my-6"></v-spacer>

                <v-main class="d-flex justify-center align-center">
                  <img :src="ghchartsrc"/>
                </v-main>
                <!-- 个人简介 -->
                <v-main class="d-flex justify-center align-center">
                  <v-card color="grey-lighten-5" elevation="1" height="10vw" hover width="40vw">
                    <v-card-title>总结</v-card-title>
                    <v-card-text>{{ user?.bio || '代码是艺术和解决问题的途径' }}</v-card-text>
                  </v-card>
                </v-main>
                <v-spacer class="my-6"></v-spacer>
              </v-card-text>
            </v-card>
          </v-main>
          <v-spacer class="my-6"></v-spacer>
        </v-main>
      </v-parallax>
      <!-- 网站页脚 -->
      <FooterBar/>
    </v-container>
  </v-app>
</template>

<script lang="ts" setup>
import {ref} from 'vue'
import {src} from '@/public/public'
import axios from 'axios'

interface UserData {
  avatarUrl: string;
  name: string;
  username: string;
  company: string | null;
  location: string | null;
  followers: number;
  following: number;
  repos: number;
  bio: string | null;
  score: number | string;
  country: string | null;
  reliability: number;
}

// 定义图标和加载状态的响应式变量
const loaded = ref(false)
const loading = ref(false)
const avatarUrl = ref('') // 用户头像 URL
const Login = ref('')
const username = ref('')
const error = ref('')
const ghchartsrc = ref('')

const user = ref<UserData | null>(null)

// 点击事件处理函数
async function onClick() {
  loading.value = true
  error.value = ''
  try {
    const response = await axios.get('/api/user', {
      params: {
        username: username.value
      }
    })
    console.log(response.data)
    const data = response.data
    // 更新用户数据
    user.value = {
      avatarUrl: data.avatar_url,
      name: data.name || data.login,
      username: data.login,
      company: data.company,
      location: data.location,
      followers: data.followers,
      following: data.following,
      repos: data.public_repos,
      bio: data.bio,
      score: Math.round(data.score * 100) / 100,
      country: data.country,
      reliability: data.reliability
    }
    avatarUrl.value = data.avatar_url
    Login.value = data.login
    ghchartsrc.value = 'https://ghchart.rshah.org/' + data.login
    loaded.value = true
  } catch (err) {
    console.error(err)
    // 如果后端返回错误信息，则将其赋值给 error.value
    if (axios.isAxiosError(err)) {
      // 如果错误是由 axios 发出的，则尝试提取详细错误信息
      if (err.response && err.response.data && err.response.data.error) {
        error.value = err.response.data.error;
      } else if (err.message) {
        // 如果没有具体的 response 数据，但有一般错误信息
        error.value = err.message;
      } else {
        error.value = '发生了一个未知错误。';
      }
    } else if (err instanceof Error) {
      // 如果 err 是标准的 JavaScript 错误对象
      error.value = err.message;
    } else {
      // 最后处理任何无法识别的错误对象
      error.value = '发生了一个未知错误。';
    }
    loaded.value = false
  } finally {
    loading.value = false
  }
}

// 错误消息被点击时的处理函数
function onErrorDismissed() {
  error.value = ''
}
</script>

<style>
.avatar-img {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover; /* 保持图片宽高比 */
}

.text-black {
  color: black;
}

.font-weight-bold {
  font-weight: bold;
}
</style>
