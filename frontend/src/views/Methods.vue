<template>
  <div class="min-h-screen bg-background">
    <!-- Hero Section -->
    <section class="py-20 px-4 bg-gradient-to-b from-background to-muted/20">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-16">
          <h1 class="text-4xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-primary to-primary/70 bg-clip-text">
            Методики
          </h1>
        </div>

         <!-- Методики по отраслям -->
         <div class="space-y-12">
           <MethodBlock
             v-for="method in methods"
             :key="method.title"
             :method="method"
           />
         </div>


       
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import MethodBlock from "@/components/MethodBlock.vue";

interface MethodItem {
  title: string;
  image: string;
  link: string;
  items: {
    text: string;
    image: string;
    link: string;
  }[];
}

const methods: MethodItem[] = [
  {
    title: "Методики анализа нефти и нефтепродуктов",
    image: "/лого-методик/Газ овая промышленность/Определение общей серы в природном и углеводородных газах.png",
    link: "/methods-oil",
    items: [
      {
        text: "Определение серы в нефти и нефтепродуктах по ГОСТ Р ЕН ИСО 20847-2010 и ГОСТ ISO 20847-2014",
        image: "/10.png",
        link: "/methods-oil"
      },
      {
        text: "Определение серы в нефти и нефтепродуктах по ГОСТ 33194-2014",
        image: "/10.png",
        link: "/methods-oil"
      },
      {
        text: "Определение серы в нефти и нефтепродуктах по ГОСТ Р 53203-2022",
        image: "/10.png",
        link: "/methods-oil"
      },
      {
        text: "Определение серы в нефти и нефтепродуктах по ГОСТ ISO 8754-2013",
        image: "/10.png",
        link: "/methods-oil"
      },
      {
        text: "Определение серы в нефти и нефтепродуктах по ГОСТ 32139-2019",
        image: "/10.png",
        link: "/methods-oil"
      },
      {
        text: "Определение серы в нефти и нефтепродуктах по ГОСТ Р 51947-2002",
        image: "/10.png",
        link: "/methods-oil"
      },
      {
        text: "Определение серы в нефтепродуктах по ГОСТ Р ЕН ИСО 14596-2008",
        image: "/10.png",
        link: "/methods-oil"
      },
      {
        text: "Нефтепродукты. Определение серы в автомобильном топливе методом ультрафиолетовой флуоресценции по ISO 20846:2011",
        image: "/10.png",
        link: "/methods-oil"
      },
      {
        text: "Определение серы в автомобильном топливе по ГОСТ Р 52660-2006 и ГОСТ ISO 20884-16",
        image: "/10.png",
        link: "/methods-oil"
      },
      {
        text: "Нефтепродукты. Определение серы методом ультрафиолетовой флуоресценции по ASTM D5453-16",
        image: "/10.png",
        link: "/methods-oil"
      },
      {
        text: "Определение хлорорганических соединений в нефти по ГОСТ Р 52247-2021 (метод В)",
        image: "/10.png",
        link: "/methods-oil"
      },
      {
        text: "Определение свинца в автомобильном бензине по ГОСТ Р 54278-2010",
        image: "/10.png",
        link: "/methods-oil"
      },
      {
        text: "Определение Mg, Ca, S, P, Zn в маслах и присадках (ФР.1.31.2014.17348)",
        image: "/10.png",
        link: "/methods-oil"
      },
      {
        text: "Определение Pb, Fe, Mn в автомобильном бензине (ФР.1.31.2017.26861)",
        image: "/10.png",
        link: "/methods-oil"
      },
      {
        text: "Определение Pb, Zn, Ni, Fe, Mn, V в нефти и нефтепродуктах (ФР.1.31.2014.17352)",
        image: "/10.png",
        link: "/methods-oil"
      },
      {
        text: "Определение органического хлора в нафте от 1 ppm (ФР.1.31.2020.37472)",
        image: "/10.png",
        link: "/methods-oil"
      },
      {
        text: "Стандартный метод определения следов азота в жидких углеводородах по ASTM D4629-17",
        image: "/10.png",
        link: "/methods-oil"
      }
    ]
  },
  {
    title: "Методики анализа в области экологии",
    image: "/home-photo/ecologylittle.png",
    link: "/methods-eco",
    items: [
      {
        text: "Определение массовой доли элементов и оксидов элементов рентгенофлуоресцентным методом",
        image: "/10.png",
        link: "/methods-eco"
      },
      {
        text: "Рентгенофлуоресцентный анализ отходов минерального происхождения",
        image: "/10.png",
        link: "/methods-eco"
      },
      {
        text: "Определение элементов и оксидов элементов в пробах почв и донных отложений (ФР.1.31.2018.32143)",
        image: "/10.png",
        link: "/methods-eco"
      },
      {
        text: "Определение Mg, Al, Si, P, S, K, Ca, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, As, Sr, Ba, Pb в отходах минерального происхождения (ФР.1.31.2015.20702)",
        image: "/10.png",
        link: "/methods-eco"
      },
      {
        text: "Определение Mg, Al, Si, Zn, P, S, Cl, K, Ca, Ba, Ti, Cr, Mn, Fe, Ni, Br, Rb, Sr в растительных материалах и продуктах питания (ФР.1.31.2014.17343)",
        image: "/10.png",
        link: "/methods-eco"
      },
      {
        text: "Определение диоксида кремния в воздухе рабочей зоны (ФР.1.31.2014.17344)",
        image: "/10.png",
        link: "/methods-eco"
      },
      {
        text: "Определение Cd, Se, As, V, Bi, Fe, Co, Cu, Ni, Pb, Cr, Zn в пробах природных, питьевых и сточных вод (ФР.1.31.2011.09287)",
        image: "/10.png",
        link: "/methods-eco"
      },
      {
        text: "Определение элементов Mg, Al, Si, P, K, Ca, Ti, Mn, Fe, V, Cr, Co, Ni, Cu, Zn, As, Sr и Pb, а также оксидов элементов MgO, Al2O3, SiO2, P2O5, K2O, CaO, TiO2, MnO, Fe2O3 в почвах (ФР.1.31.2016.25423)",
        image: "/10.png",
        link: "/methods-eco"
      },
      {
        text: "Определение V, Bi, Fe, Co, Mn, Cu, Ni, Pb, Cr, Zn в воздухе рабочей зоны (МУК 4.1.1354-03)",
        image: "/10.png",
        link: "/methods-eco"
      },
      {
        text: "Определение Pb, Zn, Cu, Ni, Co, Fe, Mn, Cr в вентиляционных выбросах (ФР.1.31.2011.09285)",
        image: "/10.png",
        link: "/methods-eco"
      }
    ]
  },
  {
    title: "Методики анализа в горнорудной промышленности",
    image: "/home-photo/gornlittle.png",
    link: "/methods-mining",
    items: [
      {
        text: "Определение S, P, K, Ca, Si, Cl, Mn, Fe, Ti и Sr в углях (ФР.1.31.2014.17351)",
        image: "/10.png",
        link: "/methods-mining"
      },
      {
        text: "Определение Cr₂O₃, FeO, CaO, SiO₂, Al₂O₃, MgO, P₂O₅ в хромовых рудах",
        image: "/10.png",
        link: "/methods-mining"
      },
      {
        text: "Определение MgO, Al₂O₃, SiO₂, CaO, Fe₂O₃ в магнезиальных неформованных огнеупорах (ФР.1.31.2014.17347)",
        image: "/10.png",
        link: "/methods-mining"
      },
      {
        text: "Определение MgO, Al₂O₃, SiO₂, CaO, TiO₂, Fe₂O₃ в алюмосиликатных неформованных огнеупорах (ФР.1.31.2014.17346)",
        image: "/10.png",
        link: "/methods-mining"
      },
      {
        text: "Определение оксидов Na, Mg, Al, Si, P, K, Ca, Ti, Mn и Fe в железомарганцевых конкрециях (ФР.1.31.2014.17345)",
        image: "/10.png",
        link: "/methods-mining"
      }
    ]
  },
  {
    title: "Методики анализа в продукции металлургии",
    image: "/home-photo/metlittle.png",
    link: "/methods-metallurgy",
    items: [
      {
        text: "Анализ чугуна по ГОСТ Р 55080-2012",
        image: "/10.png",
        link: "/methods-metallurgy"
      },
      {
        text: "Анализ литейных латуней по ГОСТ 30609-98",
        image: "/10.png",
        link: "/methods-metallurgy"
      },
      {
        text: "Анализ стали по ГОСТ 28033-89",
        image: "/10.png",
        link: "/methods-metallurgy"
      },
      {
        text: "Определение Zr, Mo, W и Ta в сплавах на основе ниобия по ГОСТ 25278.15-87",
        image: "/10.png",
        link: "/methods-metallurgy"
      },
      {
        text: "Анализ твердых спеченных сплавов по ГОСТ 28817-90",
        image: "/10.png",
        link: "/methods-metallurgy"
      },
      {
        text: "Анализ оловянных бронз по ГОСТ 30608-98",
        image: "/10.png",
        link: "/methods-metallurgy"
      },
      {
        text: "Определение алюминия в безоловянных бронзах по ГОСТ 20068.4-88",
        image: "/10.png",
        link: "/methods-metallurgy"
      },
      {
        text: "Определение Al, Si, P, S, Ti, V, Cr, Mn, Co, Ni, Cu, Nb, Mo и W в пробах углеродистых сталей",
        image: "/10.png",
        link: "/methods-metallurgy"
      }
    ]
  },
  {
    title: "Методики анализа для диагностики и контроля",
    image: "/home-photo/diagnostikalittle2.png",
    link: "/methods-diagnostics",
    items: [
      {
        text: "Технологические водные среды атомных электростанций. Определение меди, железа, никеля, хрома, марганца, циркония, содержащихся в виде взвесей",
        image: "/10.png",
        link: "/methods-diagnostics"
      },
      {
        text: "Определение Mg, Al, Si, Ti, V, Cr, Mn, Fe, Ni, Cu, Mo, Ag, Sn, W, Pb – продуктов изнашивания и загрязнения – в пробах жидких нефтепродуктов (ФР.1.31.2015.20700)",
        image: "/10.png",
        link: "/methods-diagnostics"
      },
      {
        text: "Определение Cu, Fe, Ni, Cr, Mn и Zr, содержащихся в виде взвесей в технологических водных средах АЭС (ФР.1.31.2011.09281)",
        image: "/10.png",
        link: "/methods-diagnostics"
      },
      {
        text: "Определение Fe, Cu, Ni, Cr, Mn и Zn в шихте ионообменных смол (ФР.1.31.2011.09283)",
        image: "/10.png",
        link: "/methods-diagnostics"
      },
      {
        text: "Определение Mo, Cu и Fe в технологических водных средах (ФР.1.31.2014.18559)",
        image: "/10.png",
        link: "/methods-diagnostics"
      },
      {
        text: "Определение Ni, Cr, Mn и Co в технологических водных средах АЭС и жидких радиоактивных отходах (ФР.1.31.2011.09282)",
        image: "/10.png",
        link: "/methods-diagnostics"
      },
      {
        text: "Определение Ni, Mn, Cr, ZnO, CuO, Fe₂O₃, SO₃, P₂O₅, SiO₂, Al₂O₃, MgO, CaO в коррозионных отложениях (ФР.1.31.2014.17350)",
        image: "/10.png",
        link: "/methods-diagnostics"
      },
      {
        text: "Определение Ni, Mo, Co, Pt, Re, Fe в исходных и отработанных катализаторах (ФР.1.31.2014.17349)",
        image: "/10.png",
        link: "/methods-diagnostics"
      }
    ]
  },
  {
    title: "Методики анализа в газовой промышленности",
    image: "/home-photo/06bba93af58b01ffc5367e30d6485f7c.png",
    link: "/methods-gas",
    items: [
      {
        text: "Определение общей серы в природном газе методом ультрафиолетовой флуоресценции по ГОСТ 34712-2021",
        image: "/10.png",
        link: "/methods-gas"
      },
      {
        text: "Углеводороды газообразные и газы углеводородные сжиженные. Определение общего содержания серы методом ультрафиолетовой флуоресценции по ГОСТ Р 56866-2016",
        image: "/10.png",
        link: "/methods-gas"
      }
    ]
  }
];
</script>
