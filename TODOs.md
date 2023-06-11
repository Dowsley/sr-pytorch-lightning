# TODOs
- [X] Find a way to make prediction work -> Patches
- [X] Fix WRONG prediction directory with uppercases (as means of testing)
- [X] Get results with PSNR and SSIM via scikit learn
- [X] Write stuff
- [ ] How does DIV2K make a bicubic? Then Apply.
- [X] Save individual img results (and make a way to view them)
    - This might even give me some new insights
- [ ] Fix log_every_n_step thing (Possible improvement over repo)
- [ ] Extra at the very end: Predict newest JWST images of early universe with the best model found.

# Improvements over Repo
- [X] Breaking function call
- [ ] Fix WRONG prediction directory with uppercases (as means of testing)
- [ ] Push start_here.sh directories fix
- [ ] Allow predictions of whole images (add this as a parameter)
- [ ] Fix log_loss_after_n_steps
- [ ] Officialize test pipeline
- [ ] Parallelization over N gpus
- [ ] Add dependency "scikit-image", "opencv-python"

# Bugs
- [ ] Resolver Loss logging (mt espaçado, 500)

# Ideias pra escrita
- Planejamento de Testes
- Trabalhos Futuros
    - Insights into effectiveness of different labels
    - Better metrics for astronomical images
- Uso de Vast.ai

# FEEDBACKS
## Feedback 4th May
- UNIR tudo de comparison vs start_here
- Retreinar tudo com X2!
- Comparar resultados (metrics vs training)
    - Justificativas
    - Comparar pq os modelos falharam
- Apêndice, e incluir contribuições.
- LOGGAR GRAFICO NA MAO DE UMA VEZ POR TODAS

## Feedback 18th may
FAZER NA ORDEM!!!!!!!!!!!!!!!!
- [X] Quais os parâmetros para a rede? Para não comparar maçã com laranja. Preciso escrever sobre isso. **ASAP**.
    - [X] Pegar o sumário de cada rede.
- [X] Escrever achados
    - [X] dissertar sobre melhores e piores resultados (i.e. EDSR)
    - [ ] Comparar resultados entre si
        - [ ] Usar métrica GMS com a original (Nao consegui)
        - [ ] Usar PSNR e SSIM entre elas
- [X] Dissertação
    - [X] Referencial teórico, falar de cada rede usada, citar.
    - [X] Processo de machine learning (train e test)
    - [X] PSNR e SSIM

### EXTRA ASYNC (Não perder tempo plmds)
- [X] Treinar com outras losses
- [ ] Implementation details for each model para reproducibilidade.
- [ ] Ablation Studies
- Fazer pull requests

## Feedback atual
- Verificar se ta tudo ok com o jeito que treinei, e garantir que nao vai precisar de um rerun.
- Colocar fórmulas das métricas avaliativas

## Feedback 30th May
### Banca
- Márcio Dahia
- Érico Teixeira
- Eldrey Galindo (Banca)
- Esdras (convidado)

### Escrita
- [X] Endereçar feedbacks e reformatar
- [X] Ajeitar siglas
- [X] Fundamentação Teórica com mais cerne.
  - [X] Parte de Astronomia toda refeita, com imagens.
  - [X] Reescrever PSNR e SSIM com mais exemplos
  - [X] Rever Training & Testing (tá precisando melhorar...)
  - [X] Explicar melhor a pipeline de super-resolução
    - [X] convolutional layers?
    - [?] O que é um modelo densely connected?
    - [X] O que é Loss?
    - [X] RESNET.
    - [X] Melhor distinção entre SISR e MISR
    - [X] Falar de downscaling
    - [X] Activation functions, explicar elas
    - [ ] DIV2K
    - [ ] Adicionar referencias onde precisa...
  - [X] Escrever mais sobre os modelos
    - [X] (Mostrar e explicar o diagrama do modelo)
    - [...] Parametros (PRIORITY)
      - [...] Hiperparametros
      - [...] Quantidade de Parametros
      - [...] Reescrever algumas partes...
- [ ] Deixar claro que os parâmetros usados na rede são criados pelo trabalho de George.
    - "Para os propósitos deste trabalho, foram assumidos tal tal".
    - Ler trabalho de George.
    - Detalhes de implementação, na metodologia. Falando da quantidade de parâmetros treináveis, e não-treináveis.
- [ ] Pencil Sketch atrapalha com área das imagens
- [ ] Focar mais nas imagens -> Resultados entre elas
- [ ] Próximos passos (Por que tiveram resultados tão discrepantes no EDSR)?
- [ ] Loss Graphs
  - [ ] Falar também do que foi feito errado na pesquisa (considerações)
- [ ] Contribuições
- [ ] Citar paper de george


# Report Final:
- 
