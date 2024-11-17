<!--
 * @Author: jiang
 * @Date: 2024-11-05 16:23:25
 * @LastEditors: jiang
 * @LastEditTime: 2024-11-06 23:42:53
 * @FilePath: \MAO-MAO-SEEK-UI\MAO-MAO\src\components\Login.vue
 * @Description:
 *
 * Copyright (c) 2024 by jiang, All Rights Reserved.
-->
<template>
  <div v-if="isLoggedIn">
    <!-- 登录状态显示头像 -->
    <v-avatar class="me-2" size="40">
      <img :src="avatarUrl" alt="User Avatar" class="avatar-img" @click="confirmLogout"/>
    </v-avatar>
    <!-- 确认注销对话框 -->
    <v-dialog v-model="dialog" max-width="400px">
      <v-card>
        <v-card-title class="headline">确认注销</v-card-title>
        <v-card-text>您确定要注销吗？</v-card-text>
        <v-card-actions>
          <v-btn @click="dialog = false">取消</v-btn>
          <v-btn color="red" @click="onLogout">确认</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
  <div v-else class="pa-4 text-center">
    <!-- 未登录状态显示登录按钮 -->
    <v-btn-group color="#b2d7ef" density="comfortable" divided rounded="pill">
      <v-btn class="pe-2" variant="flat">
        <v-icon class="me-2">mdi-account-multiple-outline</v-icon>
        <div class="text-none font-weight-regular">登录</div>

        <v-dialog activator="parent" max-width="500">
          <template v-slot:default="{ isActive }">
            <v-card rounded="lg">
              <v-card-title class="d-flex justify-space-between align-center">
                <div class="text-h5 text-medium-emphasis ps-2">身份验证</div>
                <v-btn icon="mdi-close" variant="text" @click="isActive.value = false"></v-btn>
              </v-card-title>

              <v-divider class="mb-4"></v-divider>

              <v-card-text>
                <div class="text-medium-emphasis mb-4">
                  请使用GitHub应用生成的令牌进行身份验证
                </div>
                <div class="mb-2">ACCESS_TOKEN_TO_CHECK</div>

                <!-- 绑定 accessToken 到文本框 -->
                <v-textarea v-model="accessToken" :counter="300" class="mb-2" persistent-counter rows="2"
                            variant="outlined"></v-textarea>

                <div class="text-overline mb-2">💎 PREMIUM</div>

                <div class="text-medium-emphasis mb-1">
                  如果您不知道如何获取，请访问
                  <a :href="GitHubAPI" rel="noopener noreferrer" target="_blank">GitHubAPI 官方文档</a>
                </div>
              </v-card-text>

              <v-divider class="mt-2"></v-divider>

              <v-card-actions class="my-2 d-flex justify-end">
                <v-btn class="text-none" rounded="xl" text="取消" @click="isActive.value = false"></v-btn>
                <v-btn class="text-none" color="primary" rounded="xl" text="登录" variant="flat"
                       @click="() => { handleLogin(); isActive.value = false; }">
                  登录
                </v-btn>
              </v-card-actions>

            </v-card>
          </template>
        </v-dialog>
      </v-btn>
    </v-btn-group>
  </div>
  <Error v-model="isErrorVisible" :error-message="errorMessage" />
</template>

<script lang="ts" setup>
import {onMounted, ref} from 'vue'
import {GitHubAPI} from '@/public/public'
import {login} from '@/services/authService'
import Error from "@/components/Error.vue";

const isLoggedIn = ref(false) // 登录状态
const avatarUrl = ref('') // 用户头像 URL
const accessToken = ref('') // GitHub 令牌
const dialog = ref(false)
const isErrorVisible = ref(false); // 控制错误框的可见性
const errorMessage = ref(""); // 错误消息内容

// 登录处理函数
async function handleLogin() {
  const user = await login(accessToken.value)
  console.log(user)
  if (user) {
    isLoggedIn.value = true
    avatarUrl.value = user.avatar_url
    localStorage.setItem('user', JSON.stringify(user))
    localStorage.setItem('isLoggedIn', JSON.stringify(isLoggedIn.value))
  } else {
    console.error('登录失败，无法获取用户信息')
    isLoggedIn.value = false // 登录失败
    errorMessage.value = ''
    setTimeout(()=>{
      isErrorVisible.value = true
      errorMessage.value = "登录失败，发生意外错误，请稍后再试！"
    }, 10)

    // alert('登录失败，发生意外错误，请稍后再试！');
  }
}

// 页面恢复状态
onMounted(() => {
  const storedUser = localStorage.getItem('user');
  const storedIsLoggedIn = localStorage.getItem('isLoggedIn');

  if (storedUser && storedIsLoggedIn) {
    const user = JSON.parse(storedUser);
    isLoggedIn.value = JSON.parse(storedIsLoggedIn);  // 解析为布尔值
    avatarUrl.value = user.avatar_url || '';          // 从用户数据中获取 avatar URL
    console.log(`Welcome back, ${user.name}`);
  }
});

function confirmLogout() {
  dialog.value = true
}

function onLogout() {
  dialog.value = false
  isLoggedIn.value = false
  localStorage.removeItem('user');
  localStorage.removeItem('isLoggedIn')
}


</script>

<style>
.avatar-img {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
  /* 保持图片宽高比 */
}
</style>
