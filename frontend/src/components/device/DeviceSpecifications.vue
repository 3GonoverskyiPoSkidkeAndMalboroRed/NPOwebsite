<template>
  <div v-if="activeTab === 'specifications'" class="space-y-6">
    <h3 class="text-2xl font-bold mb-4">Характеристики</h3>
    
    <!-- Аналитические параметры -->
    <div v-if="analyticalParams" class="space-y-4">
      <h4 class="text-lg font-semibold">АНАЛИТИЧЕСКИЕ ПАРАМЕТРЫ</h4>
      <div class="grid md:grid-cols-2 gap-6">
        <div class="space-y-3">
          <div v-for="(param, index) in analyticalParams.left" :key="index" class="flex justify-between">
            <span >{{ param.label }}:</span>
            <span>{{ param.value }}</span>
          </div>
        </div>
        <div class="space-y-3">
          <div v-for="(param, index) in analyticalParams.right" :key="index" class="flex justify-between">
            <span class="font-medium  ">{{ param.label }}:</span>
            <span>{{ param.value }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Технические характеристики -->
    <div v-if="technicalParams" class="space-y-4">
      <h4 class="text-lg font-semibold">ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ</h4>
      <div class="grid md:grid-cols-2 gap-6">
        <div class="space-y-3">
          <div v-for="(param, index) in technicalParams.left" :key="index" class="flex justify-between">
            <span class="font-medium">{{ param.label }}:</span>
            <span>{{ param.value }}</span>
          </div>
        </div>
        <div class="space-y-3">
          <div v-for="(param, index) in technicalParams.right" :key="index" class="flex justify-between">
            <span class="font-medium">{{ param.label }}:</span>
            <span>{{ param.value }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Parameter {
  label: string;
  value: string;
}

interface Parameters {
  left: Parameter[];
  right: Parameter[];
}

interface Props {
  activeTab: string;
  analyticalParams?: Parameters;
  technicalParams?: Parameters;
}

defineProps<Props>();
</script>
