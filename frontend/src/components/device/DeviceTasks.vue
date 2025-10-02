<template>
  <div v-if="activeTab === 'tasks'" class="space-y-6">
    <h3 class="text-2xl font-bold mb-4">Решаемые задачи</h3>
    <div class="space-y-4">
      <div v-for="task in tasks" :key="task.title" class="p-6 bg-muted/30 rounded-lg">
        <h4 class="text-lg font-semibold mb-2">{{ task.title }}</h4>
        <p class="text-muted-foreground">{{ task.description }}</p>
        <div class="mt-3">
          <span class="text-sm font-medium text-primary">Применение:</span>
          <span class="text-sm ml-2">{{ task.application }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Task {
  title: string;
  description: string;
  application: string;
}

interface Props {
  activeTab: string;
  tasks: Task[];
}

defineProps<Props>();
</script>
