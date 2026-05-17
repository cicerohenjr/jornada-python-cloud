from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)

modelo_arvore = RandomForestClassifier()
modelo_arvore.fit(x_treino, y_treino)
previsao = modelo_arvore.predict(x_teste)

print(f"Acurácia do modelo preditivo: {accuracy_score(y_teste, previsao)}")
