<script setup lang="ts">
// Компонент для отображения основ рентгенофлуоресцентного анализа
</script>

<template>
  <div class="min-h-screen bg-background">
    <!-- Заголовок страницы -->
    <div class="bg-primary/5 py-16 sm:py-20">
      <div class="container px-4 sm:px-6 lg:px-8">
        <div class="max-w-4xl mx-auto text-center">
          <h1 class="text-3xl sm:text-4xl md:text-5xl font-bold mb-4">
            Основы РФА
          </h1>
          <p class="text-lg sm:text-xl text-muted-foreground max-w-2xl mx-auto">
            Теоретические основы рентгенофлуоресцентного анализа
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
              Рентгенофлуоресцентный метод относится к инструментальным методам определения элементного состава и позволяет определять валовые содержания элементов в диапазоне от B до U, безотносительно от формы их нахождения в веществе.
            </p>
            <p class="text-lg">
              Типичный диапазон определяемых содержаний для РФА составляет от n*0,0001% до 100%. Применение способов концентрирования позволяет в ряде случаев понизить предел определения еще на два порядка.
            </p>
          </div>
        </div>

        <!-- Физические основы -->
        <div class="mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Физические основы рентгенофлуоресцентного метода</h2>
          
          <div class="prose prose-sm sm:prose-base lg:prose-lg max-w-none mb-8">
            <p class="mb-4">
              Сущность рентгенофлуоресцентного метода понятна из его названия:
            </p>
            
            <div class="grid md:grid-cols-2 gap-6 mb-8">
              <div class="bg-primary/10 p-6 rounded-lg">
                <h3 class="text-lg font-semibold mb-3">«Рентгено-»</h3>
                <p class="text-sm">
                  Используется рентгеновское излучение, источником которого служит, как правило, рентгеновская трубка. Все современные приборы, реализующие рентгенофлуоресцентный метод и предназначенные для массового применения, используют в качестве источника первичного излучения рентгеновскую трубку.
                </p>
              </div>
              
              <div class="bg-primary/10 p-6 rounded-lg">
                <h3 class="text-lg font-semibold mb-3">«Флуоресцентный»</h3>
                <p class="text-sm">
                  Используется флуоресценция атомов пробы – вторичное рентгеновское излучение в области длин волн (от десятых долей до десятков ангстрем), вызванное первичным рентгеновским излучением рентгеновской трубки.
                </p>
              </div>
            </div>
          </div>

          <div class="bg-muted/50 p-6 rounded-lg mb-8">
            <h3 class="text-xl font-semibold mb-4">Как возбуждается флуоресцентное излучение?</h3>
            <p class="mb-4">
              В результате взаимодействия первичного излучения с веществом пробы происходит либо рассеяние первичных квантов на атомах элементов, составляющих пробу, либо удаление электрона с одной из внутренних атомных оболочек. В последнем случае атом оказывается в возбуждённом состоянии. Избыток энергии сбрасывается в виде кванта флуоресцентного (характеристического) излучения.
            </p>
            
            <div class="bg-background p-4 rounded-lg">
              <p class="text-sm font-medium mb-2">Вакансия, возникшая в одной из оболочек, может быть заполнена электронами различных энергетических уровней атома.</p>
              <p class="text-sm mb-2">Все линии спектра, появляющиеся при таких переходах, образуют одну серию линий, обозначаемую так же, как и оболочка начального состояния (K, L, M, N, O, P).</p>
              <p class="text-sm mb-2">Линии K-серии – наиболее коротковолновые, далее в порядке возрастания длин волн расположены L, M, N-серии.</p>
              <p class="text-sm">Самые интенсивные линии серии - α, затем в порядке убывания β и γ.</p>
            </div>
          </div>

          <div class="bg-primary/10 p-6 rounded-lg">
            <p class="text-center font-medium">
              При этом атомы каждого химического элемента излучают кванты со строго определенной энергией, которая фактически не зависит от химического строения вещества. По этой причине вторичное флуоресцентное излучение атома также называют характеристическим излучением.
            </p>
          </div>
        </div>

        <!-- Основные типы приборов -->
        <div class="mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Основные типы приборов для РФА</h2>
          
          <div class="grid md:grid-cols-2 gap-8">
            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4">Спектрометры с волновой дисперсией (WDS)</h3>
              <p class="text-sm mb-4">
                В этом типе приборов для выделения вторичного излучения с той или иной длиной волны используют дифракцию рентгеновского излучения на кристаллической решётке.
              </p>
              <div class="space-y-2">
                <div class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span class="text-sm">Высокая способность к разделению спектральных линий</span>
                </div>
                <div class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span class="text-sm">Точный анализ сложных многокомпонентных веществ</span>
                </div>
                <div class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span class="text-sm">Кристалл-дифракционный способ разложения</span>
                </div>
              </div>
            </div>
            
            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-xl font-semibold mb-4">Спектрометры с энергетической дисперсией (EDS)</h3>
              <p class="text-sm mb-4">
                В этом типе для регистрации вторичного излучения используют специальные детекторы, электрический сигнал которых пропорционален энергии рентгеновского излучения.
              </p>
              <div class="space-y-2">
                <div class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span class="text-sm">Амплитудная селекция для выделения участка спектра</span>
                </div>
                <div class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span class="text-sm">Значительная степень наложения соседних линий</span>
                </div>
                <div class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span class="text-sm">Осложняет анализ многокомпонентных веществ</span>
                </div>
              </div>
            </div>
          </div>

          <div class="bg-primary/10 p-6 rounded-lg mt-8">
            <h3 class="text-xl font-semibold mb-4">Спектрометры НПО «СПЕКТРОН»</h3>
            <p class="mb-4">
              Производимые НПО «СПЕКТРОН» спектрометры «СПЕКТРОСКАН МАКС» относятся к волнодисперсионным спектрометрам. Главной их отличительной особенностью является применение светосильной кристалл-дифракционной рентгенооптической схемы по Иоганссону.
            </p>
            <div class="grid md:grid-cols-2 gap-4">
              <div>
                <h4 class="font-semibold mb-2">Преимущества:</h4>
                <ul class="space-y-1 text-sm">
                  <li>• Расположение рентгеновской трубки максимально близко к образцу</li>
                  <li>• Высокая фокусирующая способность</li>
                  <li>• Использование маломощных рентгеновских трубок (4-160 Вт)</li>
                  <li>• Размеры настольного устройства</li>
                </ul>
              </div>
              <div>
                <h4 class="font-semibold mb-2">Возможности:</h4>
                <ul class="space-y-1 text-sm">
                  <li>• Не уступают по способности разделения линий</li>
                  <li>• Высокая чувствительность</li>
                  <li>• Анализ сложных многокомпонентных веществ</li>
                  <li>• Точные аналитические результаты</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <!-- Преимущества РФА -->
        <div class="mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Преимущества рентгенофлуоресцентного метода</h2>
          
          <div class="grid md:grid-cols-2 gap-6">
            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-3">1. Анализ без растворения</h3>
              <p class="text-sm">
                Возможность анализа твердых проб без переведения их в раствор, а также возможность анализа жидких проб без отделения органической составляющей.
              </p>
            </div>
            
            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-3">2. Простота спектра</h3>
              <p class="text-sm">
                Простота и однозначность рентгеновского спектра. Наличие характеристического спектра является прямым доказательством присутствия элемента.
              </p>
            </div>
            
            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-3">3. Неразрушающий характер</h3>
              <p class="text-sm">
                Позволяет анализировать уникальные пробы и пробы, существующие в единичном экземпляре, например предметы искусства.
              </p>
            </div>
            
            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-3">4. Широкие возможности</h3>
              <p class="text-sm">
                Диапазон определяемых содержаний от n*1,0 мг/кг до 100% без концентрирования проб и от n*0,01 мг/кг с концентрированием.
              </p>
            </div>
          </div>

          <div class="bg-muted/50 p-6 rounded-lg mt-8">
            <h3 class="text-xl font-semibold mb-4">Дополнительные возможности РФА:</h3>
            <div class="grid md:grid-cols-2 gap-4">
              <div>
                <ul class="space-y-2">
                  <li class="flex items-start">
                    <span class="text-primary mr-2 flex-shrink-0">•</span>
                    <span class="text-sm">Определение общего содержания аналита вне зависимости от формы нахождения</span>
                  </li>
                  <li class="flex items-start">
                    <span class="text-primary mr-2 flex-shrink-0">•</span>
                    <span class="text-sm">Определение в одном эксперименте основных и примесных элементов</span>
                  </li>
                </ul>
              </div>
              <div>
                <ul class="space-y-2">
                  <li class="flex items-start">
                    <span class="text-primary mr-2 flex-shrink-0">•</span>
                    <span class="text-sm">Проведение локального анализа с локальностью от нескольких десятков мкм</span>
                  </li>
                  <li class="flex items-start">
                    <span class="text-primary mr-2 flex-shrink-0">•</span>
                    <span class="text-sm">Анализ без вакуумирования образца</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <!-- Количественный анализ -->
        <div class="mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Количественный анализ</h2>
          
          <div class="prose prose-sm sm:prose-base lg:prose-lg max-w-none mb-8">
            <p class="mb-4">
              Между интенсивностью линии (Ii) и содержанием в пробе элемента (Ci), которому эта линия принадлежит, существует зависимость, близкая к пропорциональной. Для проведения анализа выбирают одну из нескольких линий флуоресценции элемента, которую называют аналитической.
            </p>
            
            <div class="bg-muted/50 p-6 rounded-lg mb-6">
              <h3 class="text-lg font-semibold mb-4">Основная зависимость:</h3>
              <div class="bg-background p-4 rounded-lg">
                <p class="text-center font-mono text-lg mb-2">I<sub>i</sub> = C<sub>i</sub> × F<sub>i</sub>(C<sub>μ</sub>, P<sub>μ</sub>)</p>
                <p class="text-sm text-center text-muted-foreground">
                  где F<sub>i</sub>(C<sub>μ</sub>, P<sub>μ</sub>) - сложная функция множества содержаний элементов и физических констант
                </p>
              </div>
            </div>
            
            <p class="mb-4">
              Проще говоря, величина сигнала от определяемого элемента зависит не только от содержания этого элемента, но и от содержаний всех остальных элементов.
            </p>
          </div>

          <div class="grid md:grid-cols-2 gap-6">
            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-3">Градуировочная характеристика</h3>
              <p class="text-sm mb-4">
                Наиболее часто применяется способ перевода Ii в Ci путем построения градуировочной характеристики (ГХ) по набору СО, аналогичным по составу пробам.
              </p>
              <div class="bg-background p-3 rounded">
                <p class="text-sm font-mono text-center">
                  C<sub>i</sub> = a<sub>0</sub> + a<sub>1</sub>I<sub>i</sub> ± a<sub>2</sub>I<sub>i</sub><sup>2</sup> - a<sub>3</sub>I<sub>i</sub> ± a<sub>4</sub>I<sub>i</sub>I<sub>j</sub> ± a<sub>5</sub>I<sub>j</sub><sup>2</sup>
                </p>
              </div>
            </div>
            
            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-3">Факторы уравнения:</h3>
              <ul class="space-y-2 text-sm">
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">±</span>
                  <span>I<sub>i</sub><sup>2</sup> - нелинейность градуировочной зависимости</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">-</span>
                  <span>I<sub>j</sub> - наложение линии j-го элемента на линию i-го</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">±</span>
                  <span>I<sub>i</sub>I<sub>j</sub> - избирательное возбуждение или поглощение</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">±</span>
                  <span>I<sub>j</sub><sup>2</sup> - наложение линий высокого порядка</span>
                </li>
              </ul>
            </div>
          </div>

          <div class="bg-muted/50 p-6 rounded-lg mt-6">
            <h3 class="text-lg font-semibold mb-4">Способ фундаментальных параметров</h3>
            <p class="text-sm mb-4">
              Вторым часто применяющимся на практике способом количественного анализа является способ фундаментальных параметров, который состоит в решении системы уравнений с условием:
            </p>
            <div class="bg-background p-4 rounded-lg text-center">
              <p class="font-mono text-lg">∑C<sub>i</sub> = 1</p>
              <p class="text-sm text-muted-foreground mt-2">где m - число элементов, составляющих пробу</p>
            </div>
            <p class="text-sm mt-4">
              Сумма содержаний всех определенных элементов должна равняться 100%. Этот способ прекрасно работает для сплавов и материалов с не слишком сложным компонентным составом.
            </p>
          </div>
        </div>

        <!-- Особенности применения -->
        <div class="mb-12">
          <h2 class="text-2xl sm:text-3xl font-bold mb-8 text-center">Особенности применения РФА</h2>
          
          <div class="space-y-6">
            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-3">Толщина слоя пробы</h3>
              <p class="text-sm mb-4">
                Толщина слоя пробы, с которого выходит излучение определяемого элемента, определяется составом этого слоя и величиной энергии излучения определяемого элемента.
              </p>
              <div class="grid md:grid-cols-2 gap-4">
                <div class="bg-background p-4 rounded-lg">
                  <h4 class="font-medium mb-2">Тяжелые элементы</h4>
                  <p class="text-sm">При использовании коротковолновых аналитических линий достаточно измельчить пробу до крупности зерен порядка 70 мкм.</p>
                </div>
                <div class="bg-background p-4 rounded-lg">
                  <h4 class="font-medium mb-2">Легкие элементы</h4>
                  <p class="text-sm">Необходимо добиваться тем меньшего размера зерен, чем меньше атомный номер определяемого элемента.</p>
                </div>
              </div>
            </div>

            <div class="bg-primary/10 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-3">Влияние минерального состава</h3>
              <p class="text-sm mb-4">
                В зависимости от того, в каком минерале содержится определяемый элемент, можно получать разную величину аналитического сигнала при одном содержании элемента.
              </p>
              <div class="space-y-2">
                <div class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span class="text-sm">Некоторые минералы приобретают ориентацию при прессовании</span>
                </div>
                <div class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span class="text-sm">Обволакивание твердых частиц более мягкими частицами</span>
                </div>
                <div class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span class="text-sm">Разная величина сигнала при разном положении образца</span>
                </div>
              </div>
            </div>

            <div class="bg-muted/50 p-6 rounded-lg">
              <h3 class="text-lg font-semibold mb-3">Сплавление проб</h3>
              <p class="text-sm mb-4">
                Принципиальное решение указанных проблем возможно только при переводе пробы в стекло. При сплавлении пробы с боратным флюсом разрушаются все минералы и частицы, образуется однородное аморфное стекло.
              </p>
              <div class="grid md:grid-cols-2 gap-4">
                <div>
                  <h4 class="font-medium mb-2">Преимущества:</h4>
                  <ul class="space-y-1 text-sm">
                    <li>• Разрушение всех минералов</li>
                    <li>• Образование однородного стекла</li>
                    <li>• Высокая точность определения</li>
                    <li>• Широкое применение в промышленности</li>
                  </ul>
                </div>
                <div>
                  <h4 class="font-medium mb-2">Недостатки:</h4>
                  <ul class="space-y-1 text-sm">
                    <li>• Разбавление пробы минимум в 2 раза</li>
                    <li>• Ухудшение пределов определения</li>
                    <li>• Дополнительные затраты времени</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Влияние состава пробы -->
        <div class="bg-primary/10 p-6 rounded-lg">
          <h2 class="text-xl font-semibold mb-4 text-center">Влияние состава пробы на метрологические характеристики анализа</h2>
          <div class="grid md:grid-cols-2 gap-6">
            <div>
              <h3 class="font-semibold mb-3">Факторы, влияющие на предел определения:</h3>
              <ul class="space-y-2 text-sm">
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Тип вещества, в котором определяется элемент</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Атомный номер элемента</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Средний атомный номер материала пробы</span>
                </li>
              </ul>
            </div>
            <div>
              <h3 class="font-semibold mb-3">Общие закономерности:</h3>
              <ul class="space-y-2 text-sm">
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Легкие элементы определяются хуже тяжелых</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Один элемент лучше определяется в легкой матрице</span>
                </li>
                <li class="flex items-start">
                  <span class="text-primary mr-2 flex-shrink-0">•</span>
                  <span>Предел определения имеет смысл только относительно вещества</span>
                </li>
              </ul>
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

.prose h3 {
  color: inherit;
  margin-top: 0;
  margin-bottom: 1rem;
}

.prose h4 {
  color: inherit;
  margin-top: 0;
  margin-bottom: 0.75rem;
}
</style>
