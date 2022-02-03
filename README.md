# Solar_Nbody_system


Solar N-body interaction system


Re-implementation my previous N-body interaction solar system assignment as object-oriented style


객체로 지정할 것:
- 행성들

N-body interaction 어떻게 구현? 

- 행성들 2차원 평면상에 놓여있다고 가정
- x축 (y=0)에 초기거리/초기속도 주어짐
- 한 행성마다 "본인을 제외하고" 다음 스텝 위치를 RK4로 계산
- 이 때 다음 스텝 위치를 임시로 저장해놓고, 다음 행성을 계산 (계산이 전부 끝날 때 까지 행성 이동 x, 각자 다음 위치 시뮬레이션만 해보기) 
- 수성부터 헬리혜성까지 전부 다 다음 위치, 다음 속도 계산했으면 한 번에 현재 위치 업데이트 + plot
- 전체 t_end에 대해서 반복해서 수행

예상 결과:

- Comet Halley의 궤적이 Chaotic한 것 처럼 나올 것. 
