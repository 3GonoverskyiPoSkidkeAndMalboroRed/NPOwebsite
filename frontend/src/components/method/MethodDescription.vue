<template>
  <div class="bg-white">
    <div class="max-w-4xl mx-auto px-4 py-6">
      <div class="prose prose-lg max-w-none">
        <p class="text-gray-700 leading-relaxed mb-4">
          {{ standardsDescription }}
        </p>
        <p class="text-gray-700 leading-relaxed">
          {{ methodDescription }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  standardsDescription: string;
  methodDescription: string;
}

defineProps<Props>();
</script>
