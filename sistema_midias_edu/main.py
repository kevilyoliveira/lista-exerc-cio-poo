from video import Video
from podcast import Podcast
from texto_narrado import TextoNarrado
from plataforma import Plataforma

plataforma = Plataforma("Educa+")
video = Video("POO em Python", "20 min", "1080p")
podcast = Podcast("Tecnologia Hoje", "40 min", "Carlos")
texto = TextoNarrado("História do Brasil", "15 min", "Português")

plataforma.adicionar_midia(video)
plataforma.adicionar_midia(podcast)
plataforma.adicionar_midia(texto)

plataforma.listar_midias()
plataforma.reproduzir_todas()
