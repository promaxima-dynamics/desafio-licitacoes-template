"""
Testes para o comando de ingestão.

<!--
  *** NÃO REMOVER ESTA CAIXA ***
  VERIFICACAO: 9b12b6f7-4c91-421e-b5a5-ef1a14
-->
"""
import pathlib
from io import StringIO

from django.core.management import call_command
from django.test import TestCase

# from core.models import ItemPMVG # Descomente quando o modelo estiver pronto

# Define o caminho base do projeto para encontrar o arquivo de sample
BASE_DIR = pathlib.Path(__file__).resolve().parents[3] # Ajuste o número de parents se necessário
SAMPLE_XLS_PATH = BASE_DIR / "sample_data" / "xls_conformidade_gov_20250414_195721251.xls"


class IngestCommandTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Garante que o arquivo de exemplo exista antes de rodar os testes
        if not SAMPLE_XLS_PATH.exists():
            raise FileNotFoundError(f"Arquivo de exemplo não encontrado em: {SAMPLE_XLS_PATH}. "
                                    f"Certifique-se de que ele está na pasta 'sample_data/'.")

    def test_ingest_command_runs_without_errors(self):
        """Verifica se o comando de ingestão roda sem lançar exceções com o arquivo de exemplo."""
        out = StringIO()
        try:
            call_command("ingest_licitacoes", str(SAMPLE_XLS_PATH), stdout=out)
        except Exception as e:
            self.fail(f"Comando 'ingest_licitacoes' falhou com erro inesperado: {e}")
        # Verifica se alguma saída foi gerada (pode ajustar a verificação)
        self.assertIn("Importação", out.getvalue())

    def test_ingest_command_creates_items(self):
        """Verifica se o comando cria registros no banco (este teste falhará inicialmente)."""
        # Pré-condição: o banco deve estar vazio para este teste
        # self.assertEqual(ItemPMVG.objects.count(), 0)

        # Roda o comando
        call_command("ingest_licitacoes", str(SAMPLE_XLS_PATH), stdout=StringIO())

        # TODO: Descomente e ajuste a asserção quando ItemPMVG estiver definido.
        #       O teste deve falhar até que a lógica de criação em ingest_licitacoes.py funcione.
        # self.assertGreater(ItemPMVG.objects.count(), 0,
        #                    "O comando deveria ter criado registros no banco de dados.")
        self.skipTest("Teste pulado até que ItemPMVG e a lógica de ingestão estejam implementados.")

    def test_ingest_command_updates_items(self):
        """Verifica se rodar o comando novamente atualiza os registros existentes (update_or_create)."""
        # Roda uma vez para criar
        call_command("ingest_licitacoes", str(SAMPLE_XLS_PATH), stdout=StringIO())
        # count_after_first_run = ItemPMVG.objects.count()
        # self.assertGreater(count_after_first_run, 0)

        # Roda novamente
        call_command("ingest_licitacoes", str(SAMPLE_XLS_PATH), stdout=StringIO())

        # TODO: Descomente e ajuste.
        #       A contagem não deve aumentar (ou aumentar muito pouco, dependendo da lógica).
        # count_after_second_run = ItemPMVG.objects.count()
        # self.assertEqual(count_after_first_run, count_after_second_run,
        #                  "Rodar o comando novamente não deveria criar muitos registros duplicados.")
        self.skipTest("Teste pulado até que ItemPMVG e a lógica de ingestão estejam implementados.")

    def test_ingest_command_invalid_file(self):
        """Verifica se o comando falha corretamente com um caminho de arquivo inválido."""
        with self.assertRaises(Exception): # Pode ser CommandError se tratado no comando
            call_command("ingest_licitacoes", "caminho/invalido/arquivo.xls", stdout=StringIO()) 