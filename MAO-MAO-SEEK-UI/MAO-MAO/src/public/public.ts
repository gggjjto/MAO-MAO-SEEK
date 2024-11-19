import {ref} from 'vue';

interface Tab {
  id: number;
  name: string;
  href: string;
}

export const tabs = ref<Tab[]>([
  {id: 1, name: '主页', href: '/'},
  {id: 2, name: '查询', href: '/search'},
  {id: 3, name: '排名', href: '/rank'},
]);
export const src = ref('../public/home.png')

interface icon {
  id: number;
  icon: string;
  src: string;
}

export const icons = ref<icon[]>([
  {id: 1, icon: 'mdi-github', src: 'https://github.com/gggjjto/MAO-MAO-SEEK'},
]);

export const GitHubAPI = ref('https://docs.github.com/zh/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28#authenticating-with-a-token-generated-by-an-app')
