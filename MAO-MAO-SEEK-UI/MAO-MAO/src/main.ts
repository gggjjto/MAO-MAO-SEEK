/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import {registerPlugins} from '@/plugins'

// Components
import App from './App.vue'

// Composables
import {createApp} from 'vue'
import HeadBar from '@/components/HeadBar.vue'
import FooterBar from '@/components/FooterBar.vue'

const app = createApp(App)

// 全局注册 HeadBar, FooterBar 组件
app.component('HeadBar', HeadBar)
app.component('FooterBar', FooterBar)

registerPlugins(app)

app.mount('#app')
