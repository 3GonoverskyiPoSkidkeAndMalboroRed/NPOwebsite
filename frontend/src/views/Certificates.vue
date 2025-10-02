<script setup lang="ts">
// Компонент для отображения сертификатов и лицензий
</script>

<template>
  <div class="min-h-screen bg-background">
    <!-- Заголовок страницы -->
    <div class="bg-primary/5 py-16 sm:py-20">
      <div class="container px-4 sm:px-6 lg:px-8">
        <div class="max-w-4xl mx-auto text-center">
          <h1 class="text-3xl sm:text-4xl md:text-5xl font-bold mb-4">
            Сертификаты и лицензии
          </h1>
          <p class="text-lg sm:text-xl text-muted-foreground max-w-2xl mx-auto">
            Все необходимые лицензии и сертификаты для производства и эксплуатации аналитического оборудования
          </p>
        </div>
      </div>
    </div>

    <!-- Основной контент -->
    <div class="container px-4 sm:px-6 lg:px-8 py-16">
      <div class="max-w-4xl mx-auto">
        
        <!-- Введение -->
        <div class="prose prose-sm sm:prose-base lg:prose-lg max-w-none mb-12">
          <div class="bg-muted/50 p-6 rounded-lg">
            <p class="text-lg font-medium mb-4">
              Научно-производственное объединение «СПЕКТРОН» обладает всеми необходимыми лицензиями и сертификатами, лицензиями на производство и ремонт средств измерений, работу с источниками ионизирующего излучения.
            </p>
          </div>
        </div>

        <!-- Основные сертификаты -->
        <div class="mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Наши сертификаты</h2>
          
          <div class="grid md:grid-cols-2 gap-6">
            <div class="bg-primary/10 p-6 rounded-lg">
              <div class="flex items-start mb-4">
                <div class="w-12 h-12 bg-primary text-primary-foreground rounded-full flex items-center justify-center mr-4 flex-shrink-0">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <div>
                  <h3 class="text-lg font-semibold mb-2">Государственный реестр средств измерений РФ</h3>
                  <p class="text-sm text-muted-foreground">
                    Наши спектрометры и анализаторы прошли всю необходимую сертификацию, внесены в Государственный реестр средств измерений РФ и имеют соответствующие сертификаты утверждения типа, снабжены сертификатами соответствия.
                  </p>
                </div>
              </div>
            </div>

            <div class="bg-primary/10 p-6 rounded-lg">
              <div class="flex items-start mb-4">
                <div class="w-12 h-12 bg-primary text-primary-foreground rounded-full flex items-center justify-center mr-4 flex-shrink-0">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                  </svg>
                </div>
                <div>
                  <h3 class="text-lg font-semibold mb-2">Освобождение от рентгеновского контроля</h3>
                  <p class="text-sm text-muted-foreground">
                    Наши приборы полностью освобождены от контроля по рентгеновскому фактору. Не требуется ни сертификация помещения, ни регистрация прибора в органах Санэпиднадзора.
                  </p>
                </div>
              </div>
            </div>

            <div class="bg-primary/10 p-6 rounded-lg">
              <div class="flex items-start mb-4">
                <div class="w-12 h-12 bg-primary text-primary-foreground rounded-full flex items-center justify-center mr-4 flex-shrink-0">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
                  </svg>
                </div>
                <div>
                  <h3 class="text-lg font-semibold mb-2">Аттестация методик</h3>
                  <p class="text-sm text-muted-foreground">
                    Все наши методики прошли процедуру аттестации и снабжены соответствующими сертификатами.
                  </p>
                </div>
              </div>
            </div>

            <div class="bg-primary/10 p-6 rounded-lg">
              <div class="flex items-start mb-4">
                <div class="w-12 h-12 bg-primary text-primary-foreground rounded-full flex items-center justify-center mr-4 flex-shrink-0">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                  </svg>
                </div>
                <div>
                  <h3 class="text-lg font-semibold mb-2">Метрологическая аттестация</h3>
                  <p class="text-sm text-muted-foreground">
                    Все наши приборы проходят процедуру метрологической аттестации и снабжены свидетельством о первичной поверке.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Международные сертификаты -->
        <div class="mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Международное признание</h2>
          
          <div class="bg-muted/50 p-6 rounded-lg">
            <div class="text-center mb-6">
              <div class="w-16 h-16 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <h3 class="text-xl font-semibold mb-4">Государственные реестры средств измерений</h3>
              <p class="text-lg">
                Наши приборы внесены в Государственные реестры средств измерений таких стран, как Украина, Беларусь, Казахстан.
              </p>
            </div>
            
            <div class="grid md:grid-cols-3 gap-4 mt-6">
              <div class="bg-background p-4 rounded-lg text-center">
                <div class="w-8 h-8 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-2">
                  <span class="text-sm font-bold">У</span>
                </div>
                <p class="font-medium">Украина</p>
              </div>
              <div class="bg-background p-4 rounded-lg text-center">
                <div class="w-8 h-8 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-2">
                  <span class="text-sm font-bold">Б</span>
                </div>
                <p class="font-medium">Беларусь</p>
              </div>
              <div class="bg-background p-4 rounded-lg text-center">
                <div class="w-8 h-8 bg-primary text-primary-foreground rounded-full flex items-center justify-center mx-auto mb-2">
                  <span class="text-sm font-bold">К</span>
                </div>
                <p class="font-medium">Казахстан</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Преимущества сертификации -->
        <div class="mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Преимущества сертифицированного оборудования</h2>
          
          <div class="grid md:grid-cols-2 gap-6">
            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-3 flex items-center">
                <svg class="w-5 h-5 mr-2 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Правовая защита
              </h3>
              <p class="text-sm text-muted-foreground">
                Использование сертифицированного оборудования обеспечивает полную правовую защиту при проведении аналитических работ.
              </p>
            </div>
            
            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-3 flex items-center">
                <svg class="w-5 h-5 mr-2 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Упрощенная процедура
              </h3>
              <p class="text-sm text-muted-foreground">
                Отсутствие необходимости в сертификации помещения и регистрации в органах Санэпиднадзора значительно упрощает процесс внедрения.
              </p>
            </div>
            
            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-3 flex items-center">
                <svg class="w-5 h-5 mr-2 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Международное признание
              </h3>
              <p class="text-sm text-muted-foreground">
                Включение в реестры средств измерений нескольких стран обеспечивает международное признание результатов измерений.
              </p>
            </div>
            
            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-3 flex items-center">
                <svg class="w-5 h-5 mr-2 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Гарантия качества
              </h3>
              <p class="text-sm text-muted-foreground">
                Все сертификаты подтверждают соответствие оборудования строгим стандартам качества и метрологическим требованиям.
              </p>
            </div>
          </div>
        </div>

        <!-- Документы для скачивания -->
        <div class="bg-muted/50 p-6 rounded-lg">
          <h2 class="text-2xl font-bold mb-6 text-center">Документы для скачивания</h2>
          
          <div class="grid md:grid-cols-2 gap-4">
            <div class="bg-background p-4 rounded-lg border border-border">
              <div class="flex items-center justify-between">
                <div class="flex items-center">
                  <svg class="w-8 h-8 text-primary mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                  <div>
                    <p class="font-medium">Сертификат соответствия</p>
                    <p class="text-sm text-muted-foreground">PDF, 2.1 MB</p>
                  </div>
                </div>
                <button class="px-4 py-2 bg-primary text-primary-foreground rounded-lg hover:bg-primary/90 transition-colors">
                  Скачать
                </button>
              </div>
            </div>
            
            <div class="bg-background p-4 rounded-lg border border-border">
              <div class="flex items-center justify-between">
                <div class="flex items-center">
                  <svg class="w-8 h-8 text-primary mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                  <div>
                    <p class="font-medium">Свидетельство о поверке</p>
                    <p class="text-sm text-muted-foreground">PDF, 1.8 MB</p>
                  </div>
                </div>
                <button class="px-4 py-2 bg-primary text-primary-foreground rounded-lg hover:bg-primary/90 transition-colors">
                  Скачать
                </button>
              </div>
            </div>
            
            <div class="bg-background p-4 rounded-lg border border-border">
              <div class="flex items-center justify-between">
                <div class="flex items-center">
                  <svg class="w-8 h-8 text-primary mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                  <div>
                    <p class="font-medium">Лицензия на производство</p>
                    <p class="text-sm text-muted-foreground">PDF, 1.5 MB</p>
                  </div>
                </div>
                <button class="px-4 py-2 bg-primary text-primary-foreground rounded-lg hover:bg-primary/90 transition-colors">
                  Скачать
                </button>
              </div>
            </div>
            
            <div class="bg-background p-4 rounded-lg border border-border">
              <div class="flex items-center justify-between">
                <div class="flex items-center">
                  <svg class="w-8 h-8 text-primary mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                  <div>
                    <p class="font-medium">Аттестация методик</p>
                    <p class="text-sm text-muted-foreground">PDF, 2.3 MB</p>
                  </div>
                </div>
                <button class="px-4 py-2 bg-primary text-primary-foreground rounded-lg hover:bg-primary/90 transition-colors">
                  Скачать
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.prose {
  color: inherit;
}

.prose p {
  margin-bottom: 1rem;
  line-height: 1.7;
}
</style>
