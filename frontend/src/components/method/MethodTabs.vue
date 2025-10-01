<template>
  <div class="bg-white">
    <div class="max-w-4xl mx-auto px-4 py-6">
      <div class="flex flex-wrap gap-2">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          @click="$emit('tab-change', tab.id)"
          :class="[
            'px-4 py-2 rounded-lg font-medium transition-all duration-200 border-2',
            activeTab === tab.id
              ? 'bg-gray-800 text-white border-gray-800 shadow-lg'
              : 'bg-white text-gray-700 border-gray-300 hover:border-gray-400 hover:bg-gray-50'
          ]"
        >
          {{ tab.label }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Tab {
  id: string;
  label: string;
}

interface Props {
  tabs: Tab[];
  activeTab: string;
}

defineProps<Props>();

defineEmits<{
  'tab-change': [tabId: string]
}>();
</script>
