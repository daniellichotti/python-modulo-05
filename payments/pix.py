import uuid
import qrcode

class Pix:
  def __init__(self) -> None:
    pass

  def create_payment(self):

    #cria o pagamento de uma instituição financeira ficticia
    bank_payment_id = uuid.uuid4()

    #codigo copia e cola da instituição
    hash_payment = f'hash_payment_{bank_payment_id}'
    #gera a imagem
    img = qrcode.make(hash_payment)
    #salva a imagem
    img.save(f'static/img/qr_code_payment_{bank_payment_id}.png')

    return {
      'bank_payment_id': bank_payment_id,
      'qr_code_path': f'static/img/qr_code_payment_{bank_payment_id}',
      
    }