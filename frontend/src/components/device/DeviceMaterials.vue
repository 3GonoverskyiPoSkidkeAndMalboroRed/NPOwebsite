<template>
  <div v-if="activeTab === 'materials'" class="space-y-6">
    <h3 class="text-2xl font-bold mb-4">Материалы</h3>
    
    <div class="prose prose-lg max-w-none">
      <ul class="space-y-2">
        <li v-for="(material, index) in materials" :key="index">{{ material }}</li>
      </ul>
      
      <div class="mt-8 p-6 bg-primary/5 rounded-lg border border-primary/20">
        <h4 class="text-lg font-semibold text-primary mb-4">ТЕЛЕФОН ДЛЯ ЗАКАЗА РАСХОДНЫХ МАТЕРИАЛОВ</h4>
        <p><strong>Телефон:</strong> +7 (812) 324-15-92</p>
        <p><strong>WhatsApp / Telegram / Viber:</strong> +7 (901) 304-44-44</p>
        <p><strong>E-mail:</strong> service@spectronxray.ru</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Props {
  activeTab: string;
  materials: string[];
}

defineProps<Props>();
</script>
