<template>
  <div v-if="activeTab === 'description'" class="space-y-6">
    <h3 class="text-2xl font-bold mb-4">Описание</h3>
    <div class="prose prose-lg max-w-none">
      <p v-for="(paragraph, index) in description" :key="index">
        {{ paragraph }}
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  activeTab: string;
  description: string[];
}

defineProps<Props>();
</script>
