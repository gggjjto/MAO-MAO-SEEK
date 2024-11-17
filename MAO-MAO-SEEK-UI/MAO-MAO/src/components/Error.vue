<template>
  <!-- 错误框 -->
  <v-slide-y-transition>
    <v-main v-if="visible" class="d-flex justify-center align-center text-center" style="height: 100vh; width: 100%;">
      <v-alert
        class="text-center"
        close-icon=""
        dismissible
        style="max-width: 500px;"
        type="error"
        @click="dismiss"
      >
        {{ message }}
      </v-alert>
    </v-main>
  </v-slide-y-transition>
</template>

<script setup lang="ts">
import { ref, watch, defineProps, defineEmits } from "vue";

// Props: 接收外部传递的错误消息和可见状态
const props = defineProps({
  modelValue: {
    type: Boolean,
    required: true,
  },
  errorMessage: {
    type: String,
    default: "",
  },
});

// Emits: 通知父组件状态改变
const emit = defineEmits(["update:modelValue"]);

const visible = ref(false);
const message = ref("");

// 监听 props.modelValue 的变化
watch(
  () => props.modelValue,
  (newVal) => {
    visible.value = newVal;
    if (!newVal) message.value = ""; // 隐藏时清空消息
  }
);

// 监听 props.errorMessage 的变化
watch(
  () => props.errorMessage,
  (newMessage) => {
    message.value = newMessage;
  }
);

// 处理错误框关闭
function dismiss() {
  emit("update:modelValue", false); // 通知父组件更新 modelValue
}
</script>
