<!--
Componente principal Vue.

TODO: Substitua este conteúdo pela interface de busca e exibição dos dados da API.

VERIFICACAO: 9b12b6f7-4c91-421e-b5a5-ef1a14
-->
<template>
  <div id="app" class="container mx-auto p-4">
    <h1 class="text-3xl font-bold text-center mb-6">Monitor de Preços PMVG</h1>

    <div class="bg-gray-100 p-4 rounded shadow mb-6">
      <h2 class="text-xl font-semibold mb-3">Busca e Filtros (TODO)</h2>
      <!-- TODO: Adicionar campos de busca e filtros -->
      <input type="text" placeholder="Buscar por descrição ou laboratório..." class="border p-2 rounded w-full">
    </div>

    <div class="bg-yellow-100 p-4 rounded shadow mb-6">
      <h2 class="text-xl font-semibold mb-3">Estatísticas (TODO)</h2>
      <!-- TODO: Exibir estatísticas (min, max, mean, median) -->
      <p>Mínimo: R$ --.-- | Máximo: R$ --.-- | Média: R$ --.-- | Mediana: R$ --.--</p>
    </div>

    <div class="bg-white p-4 rounded shadow">
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-xl font-semibold">Resultados (TODO)</h2>
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Exportar Selecionados (XLS)
        </button>
      </div>
      <!-- TODO: Adicionar tabela paginada com resultados da API -->
      <p class="text-center text-gray-500">Tabela de resultados aparecerá aqui...</p>
      <!-- TODO: Adicionar paginação -->
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
// import { useMyStore } from './stores/myStore'; // Exemplo com Pinia

// TODO: Definir estado com ref() ou reactive()
const searchTerm = ref('');
const results = ref([]);
const stats = ref({});
const loading = ref(false);
const error = ref(null);

// TODO: Implementar chamadas à API (axios, fetch)
async function fetchData() {
  // loading.value = true;
  // error.value = null;
  // try {
  //   const response = await fetch('/api/items/?search=' + searchTerm.value);
  //   results.value = await response.json();
  //   // Fetch stats as well
  // } catch (err) {
  //   error.value = 'Falha ao buscar dados.';
  // } finally {
  //   loading.value = false;
  // }
  console.log("Fetch data placeholder");
}

// TODO: Chamar fetchData() quando necessário (onMounted, watch)
onMounted(() => {
  // fetchData();
});

// TODO: Implementar lógica de exportação
function exportSelected() {
  console.log("Export selected placeholder");
}

// Exemplo de uso com Pinia store (descomentar import acima)
// const store = useMyStore();
// onMounted(store.fetchItems);

</script>

<style>
/* Estilos básicos ou importe Tailwind/outra lib CSS */
/* @import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities'; */
</style> 