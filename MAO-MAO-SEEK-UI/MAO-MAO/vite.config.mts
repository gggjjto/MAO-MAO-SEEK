/*
 * @Author: jiang
 * @Date: 2024-11-05 15:34:09
 * @LastEditors: jiang
 * @LastEditTime: 2024-11-06 21:53:30
 * @FilePath: \MAO-MAO-SEEK-UI\MAO-MAO\vite.config.mts
 * @Description: 
 * 
 * Copyright (c) 2024 by jiang, All Rights Reserved. 
 */
// Plugins
import Components from 'unplugin-vue-components/vite'
import Vue from '@vitejs/plugin-vue'
import Vuetify, {transformAssetUrls} from 'vite-plugin-vuetify'
import ViteFonts from 'unplugin-fonts/vite'
import VueRouter from 'unplugin-vue-router/vite'

// Utilities
import {defineConfig} from 'vite'
import {fileURLToPath, URL} from 'node:url'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        VueRouter(),
        Vue({
            template: {transformAssetUrls},
        }),
        // https://github.com/vuetifyjs/vuetify-loader/tree/master/packages/vite-plugin#readme
        Vuetify({
            autoImport: true,
            styles: {
                configFile: 'src/styles/settings.scss',
            },
        }),
        Components(),
        ViteFonts({
            google: {
                families: [{
                    name: 'Roboto',
                    styles: 'wght@100;300;400;500;700;900',
                }],
            },
        }),
    ],
    define: {'process.env': {}},
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url)),
        },
        extensions: [
            '.js',
            '.json',
            '.jsx',
            '.mjs',
            '.ts',
            '.tsx',
            '.vue',
        ],
    },
    server: {
        port: 3000,
        proxy: {
            // 配置代理，解决跨域问题
            '/api': {
                target: 'http://localhost:5000', // 指向 Flask 后端服务器
                changeOrigin: true,
                rewrite: (path) => path.replace(/^\/api/, ''), // 重写路径，将 '/api' 去除
            },
        },
    },
})
