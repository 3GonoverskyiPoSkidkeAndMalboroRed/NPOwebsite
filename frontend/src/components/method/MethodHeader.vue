<template>
  <div class="bg-white">
    <div class="max-w-4xl mx-auto px-4 py-8">
      <h1 class="text-3xl md:text-4xl font-bold text-gray-900 mb-6 leading-tight">
        {{ title }}
      </h1>
      <div class="border-b border-gray-200"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  title: string;
}

defineProps<Props>();
</script>
