# 실행: bash TimeLLM_Money.sh
model_name=TimeLLM
train_epochs=10
learning_rate=0.01
llama_layers=4  # 32이 정배임

master_port=00097
num_process=1
batch_size=4  #16으로 하고픔
d_model=32  #토큰 임베딩 차원. 
d_ff=128  # FFN에서 확장하는 차원. d_model -> d_ff -> d_model

comment='TimeLLM-Money'

# accelerate launch --multi_gpu
accelerate launch \
  --mixed_precision bf16 \
  --num_processes $num_process \
  --main_process_port $master_port \
  --num_machines 1 \
  -- \
  run_main.py \
    --task_name long_term_forecast \
    --is_training 1 \
    --root_path ./dataset/Nasdaq100/ \
    --data_path nasdaq100.csv \
    --model_id nasdaq100_512_96 \
    --model $model_name \
    --data nasdaq100 \
    --features MS \
    --target Close \
    --seq_len 512 \
    --label_len 48 \
    --pred_len 96 \
    --factor 3 \
    --enc_in 5 \
    --dec_in 5 \
    --c_out 5 \
    --des Exp \
    --itr 1 \
    --d_model $d_model \
    --d_ff $d_ff \
    --batch_size $batch_size \
    --learning_rate $learning_rate \
    --llm_layers $llama_layers \
    --train_epochs $train_epochs \
    --model_comment $comment \
    --use_wandb \
    --wandb_iter 1 \
    --exp_name $comment \
    --project_name TimeLLM \
    --entity beaver22-seoul-national-university


#  seq_len = 논문의 Input Length (과거 시계열 길이)
#  pred_len = 논문의 Forecast Horizon (미래 예측 길이)
#  label_len = 인코더-디코더 워밍업 단계에서 사용하는 teacher-forced 미래 길이 
#  (논문에는 직접 서술되지 않으며, 구현에서 label_len=pred_len 등으로 설정)
#  factor=3 → 어텐션 연산 시 적당히 희소화
#  enc_in=7, dec_in=7 → 7개 센서 채널을 인코더·디코더에 입력
#  c_out=7 → 매 스텝마다 7개 채널을 예측