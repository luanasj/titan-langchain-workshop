const { Client, LocalAuth } = require('whatsapp-web.js');

const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: {
        headless: false,   // ✅ Abre o WhatsApp Web na tela
        args: ['--no-sandbox']
    }
});

const FLASK_API_URL = 'http://127.0.0.1:5000/question';

client.on('ready', () => {
    console.log('✅ Tudo pronto! O Bot do WhatsApp está online.');
});

client.on('message', async msg => {
    if (msg.body.startsWith('!AI ') || msg.body.startsWith('!ai ')) {
        const pergunta = msg.body.slice(4).trim();

        if (!pergunta) {
            msg.reply('❌ Por favor, digite algo após o comando. Ex: !AI Quem descobriu o Brasil?');
            return;
        }

        try {
            const response = await fetch(FLASK_API_URL + "?text=" + encodeURIComponent(pergunta))
            const resContent = await response.json()
                
            console.log('resposta',resContent)
            if (resContent && resContent.resposta) {
                await msg.reply(`🤖 *IA Responde:*\n\n${resContent.resposta}`);
            } else {
                await msg.reply('❌ A API respondeu, mas não encontrei o texto da resposta.');
            }

        } catch (error) {
            console.error('Erro ao conectar com Flask:', error.message);

            if (error.code === 'ECONNREFUSED') {
                await msg.reply('❌ Não consegui conectar ao servidor da IA. Verifique se o Python está rodando.');
            } else {
                await msg.reply('❌ Ocorreu um erro ao processar sua pergunta.');
            }
        }
    }
});

client.initialize();
