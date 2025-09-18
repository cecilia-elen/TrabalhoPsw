import base64

class ImageHandlerMixin:
 
    #Um Mixin é um bloco de código reutilizável, neste caso, a gente vai usar ele para qualquer modelo que tenha um campo de imagem binária e precise exibi-lo em templates HTML.
    # Esta variável define o nome do campo de imagem.
    # O padrão é 'IMG', que serve para Produto e Catalogo e 'foto_perfil' para Usuario.
    image_field_name = 'IMG'

    def _get_image_binary_data(self):
 
        #Método auxiliar para pegar os dados binários do campo de imagem correto. Usa getattr() para acessar o atributo do modelo dinamicamente usando o nome que definimos em 'image_field_name'.

        return getattr(self, self.image_field_name, None)

    def get_image_base64(self):
        #A função principal que seus templates vão chamar. pega os dados binários e converte para Base64.
        binary_data = self._get_image_binary_data()
        if binary_data:
            return base64.b64encode(binary_data).decode('utf-8')
        return None
    #