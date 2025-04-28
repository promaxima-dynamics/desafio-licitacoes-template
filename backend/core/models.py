"""
Modelos principais.

<!--
  *** NÃO REMOVER ESTA CAIXA ***
  VERIFICACAO: 9b12b6f7-4c91-421e-b5a5-ef1a14
-->
"""
from django.db import models


class ItemPMVG(models.Model):
    """Registro individual extraído da planilha PMVG."""

    # TODO: Defina os campos do modelo baseados nas colunas mínimas
    #       do README_sources.md e na planilha de exemplo.
    #       Use os tipos de campo apropriados (CharField, DateField, DecimalField, etc.).
    #       Certifique-se de que codigo_ggrem seja único ou use-o com update_or_create.

    descricao = models.TextField(help_text="Nome/descrição do produto")
    laboratorio = models.CharField(max_length=255, help_text="Nome do fabricante/laboratório")
    codigo_ggrem = models.CharField(max_length=50, unique=True, help_text="Código GGREM único")
    # Exemplo: data_homologacao = models.DateField()
    # Exemplo: valor_unitario = models.DecimalField(max_digits=14, decimal_places=4)

    # TODO: Adicione outros campos que julgar relevantes da planilha.

    # TODO: (Opcional) Adicione campos para versionamento/histórico,
    #       como a data de importação ou a referência da planilha origem.

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Item PMVG"
        verbose_name_plural = "Itens PMVG"
        ordering = ["descricao"]

    def __str__(self):
        return f"{self.descricao} ({self.codigo_ggrem})" 