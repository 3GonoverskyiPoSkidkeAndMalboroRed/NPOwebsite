<template>
  <div v-if="activeTab === 'advantages'" class="space-y-6">
    <h3 class="text-2xl font-bold mb-4">Преимущества</h3>
    
    <div class="prose prose-lg max-w-none">
      <div class="space-y-4">
        <div class="p-4 rounded-lg">
          <h4 class="font-semibold mb-2">Основные преимущества:</h4>
          <ul class="space-y-2">
            <li v-for="(advantage, index) in advantages" :key="index" class="flex items-start gap-2">
              <span class="w-2 h-2 bg-primary rounded-full mt-2 flex-shrink-0"></span>
              <span>{{ advantage }}</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  activeTab: string;
  advantages: string[];
}

defineProps<Props>();
</script>
