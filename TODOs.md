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

- [ ] Quais os parâmetros para a rede? Para não comparar maçã com laranja. Preciso escrever sobre isso. **ASAP**.
    - [ ] Pegar o sumário de cada rede.
- [ ] Escrever achados
    - [ ] dissertar sobre melhores e piores resultados (i.e. EDSR)
    - [ ] Comparar resultados entre si
        - [ ] Usar métrica GMS com a original
        - [ ] Usar PSNR e SSIM entre elas
- [ ] Dissertação
    - [ ] Referencial teórico, falar de cada rede usada, citar.
    - [ ] Processo de machine learning (train e test)
    - [ ] PSNR e SSIM

### EXTRA ASYNC (Não perder tempo plmds)
- [ ] Treinar com outras losses
- [ ] Implementation details for each model para reproducibilidade.
- [ ] Ablation Studies