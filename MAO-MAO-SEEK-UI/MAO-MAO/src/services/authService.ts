/*
 * @Author: jiang
 * @Date: 2024-11-06 20:29:17
 * @LastEditors: jiang
 * @LastEditTime: 2024-11-06 22:20:54
 * @FilePath: \MAO-MAO-SEEK-UI\MAO-MAO\src\services\authService.ts
 * @Description:
 *
 * Copyright (c) 2024 by jiang, All Rights Reserved.
 */
import axios from 'axios';

interface User {
  login: string;
  avatar_url: string;
}

// const apiBaseURL = 'http://localhost:5000'; // 基础 API URL

// 登录函数，发送 token 给后端并返回用户信息
export async function login(token: string): Promise<User | null> {
  try {
    if (!token) {
      console.error('Token 不存在');
      return null;
    }
    console.log('正在请求登录，使用的 token:', token);

    const response = await axios.get('/api/login', {
      params: {
        token: token
      }
    });

    console.log('后端响应:', response);

    if (response.status === 200 && response.data) {
      return response.data as User;
    } else {
      console.error('无法获取用户信息', response.status);
      return null;
    }
  } catch (error) {
    // console.error('登录失败', error.response ? error.response.data : error.message);
    return null;
  }
}

// 注销函数
export function logout(): void {
  // 调用后端的注销 API 或者清除前端存储的用户信息
  console.log('用户已注销');
}
