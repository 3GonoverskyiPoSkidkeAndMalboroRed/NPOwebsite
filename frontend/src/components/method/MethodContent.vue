<template>
  <div class="bg-white">
    <div class="max-w-4xl mx-auto px-4 py-6">
      <!-- Описание методики -->
      <div v-if="activeTab === 'description'" class="prose prose-lg max-w-none">
        <h3 class="text-xl font-semibold text-gray-900 mb-4">Описание методики</h3>
        <div class="space-y-4 text-gray-700">
          <p v-for="paragraph in descriptionContent" :key="paragraph" class="leading-relaxed">
            {{ paragraph }}
          </p>
        </div>
      </div>

      <!-- Диапазон измерений -->
      <div v-if="activeTab === 'range'" class="prose prose-lg max-w-none">
        <h3 class="text-xl font-semibold text-gray-900 mb-4">Диапазон измерений</h3>
        <div class="space-y-4 text-gray-700">
          <div v-if="limitations" class="bg-yellow-50 border-l-4 border-yellow-400 p-4 mb-4">
            <h4 class="font-semibold text-yellow-800 mb-2">Ограничения:</h4>
            <p class="text-yellow-700">{{ limitations }}</p>
          </div>
          <div v-if="procedure" class="bg-blue-50 border-l-4 border-blue-400 p-4">
            <h4 class="font-semibold text-blue-800 mb-2">Процедура:</h4>
            <ul class="text-blue-700 space-y-2">
              <li v-for="step in procedure" :key="step" class="flex items-start">
                <span class="text-blue-500 mr-2">•</span>
                <span>{{ step }}</span>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Документация -->
      <div v-if="activeTab === 'documentation'" class="prose prose-lg max-w-none">
        <h3 class="text-xl font-semibold text-gray-900 mb-4">Документация</h3>
        <div class="space-y-4 text-gray-700">
          <div v-for="doc in documentation" :key="doc.title" class="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
            <h4 class="font-semibold text-gray-900 mb-2">{{ doc.title }}</h4>
            <p class="text-gray-600 mb-2">{{ doc.description }}</p>
            <a 
              v-if="doc.link" 
              :href="doc.link" 
              class="text-blue-600 hover:text-blue-800 underline"
              target="_blank"
            >
              Скачать документ
            </a>
          </div>
        </div>
      </div>

      <!-- Дополнительное оборудование -->
      <div v-if="activeTab === 'equipment'" class="prose prose-lg max-w-none">
        <h3 class="text-xl font-semibold text-gray-900 mb-4">Дополнительное оборудование</h3>
        <div class="space-y-4 text-gray-700">
          <div v-for="item in equipment" :key="item.name" class="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
            <h4 class="font-semibold text-gray-900 mb-2">{{ item.name }}</h4>
            <p class="text-gray-600 mb-2">{{ item.description }}</p>
            <div v-if="item.specifications" class="text-sm text-gray-500">
              <strong>Характеристики:</strong> {{ item.specifications }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Documentation {
  title: string;
  description: string;
  link?: string;
}

interface Equipment {
  name: string;
  description: string;
  specifications?: string;
}

interface Props {
  activeTab: string;
  descriptionContent?: string[];
  limitations?: string;
  procedure?: string[];
  documentation?: Documentation[];
  equipment?: Equipment[];
}

defineProps<Props>();
</script>
