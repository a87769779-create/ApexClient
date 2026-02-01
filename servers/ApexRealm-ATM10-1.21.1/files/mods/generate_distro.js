const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

/**
 * КОНФИГУРАЦИЯ
 */
const CONFIG = {
    baseDir: './', // Папка, где лежат Mod и files
    baseUrl: 'https://apexrealm.ru/launcher/',
    minecraftVersion: '1.21.1',
    serverId: 'ApexRealm-ATM10',
    serverName: 'ApexRealm ATM 10'
};

function getMD5(filePath) {
    const fileBuffer = fs.readFileSync(filePath);
    const hashSum = crypto.createHash('md5');
    hashSum.update(fileBuffer);
    return hashSum.digest('hex');
}

function generateDistro() {
    const distro = {
        version: "1.0.0",
        discord: {
            clientId: "000000000000000000",
            smallImageText: "ApexRealm",
            smallImageKey: "apexrealm-icon"
        },
        rss: "https://apexrealm.ru/api/rss",
        servers: [
            {
                id: CONFIG.serverId,
                name: CONFIG.serverName,
                description: "Основной сервер ApexRealm с модпаком All The Mods 10.",
                icon: CONFIG.baseUrl + "assets/server-icon.png",
                version: "1.0.0",
                address: "play.apexrealm.ru",
                minecraftVersion: CONFIG.minecraftVersion,
                discord: {
                    shortId: "ApexRealm",
                    largeImageText: CONFIG.serverName,
                    largeImageKey: "apexrealm-server"
                },
                mainServer: true,
                autoconnect: true,
                javaOptions: {
                    supported: ">=21",
                    suggestedMajor: 21
                },
                modules: []
            }
        ]
    };

    const modules = distro.servers[0].modules;

    // 1. Добавляем NeoForge если он есть в files/
    const forgePath = path.join(CONFIG.baseDir, 'files', 'neoforge-21.1.90.jar');
    if (fs.existsSync(forgePath)) {
        console.log('Добавляю NeoForge...');
        modules.push({
            id: "net.neoforged:neoforge:21.1.90",
            name: "NeoForge",
            type: "ForgeHosted",
            artifact: {
                size: fs.statSync(forgePath).size,
                MD5: getMD5(forgePath),
                url: CONFIG.baseUrl + "files/neoforge-21.1.90.jar"
            },
            subModules: []
        });
    }

    // 2. Сканируем папку Mod/
    const modsDir = path.join(CONFIG.baseDir, 'Mod');
    if (fs.existsSync(modsDir)) {
        const files = fs.readdirSync(modsDir);
        console.log(`Найдено ${files.length} файлов в папке Mod. Обработка...`);

        files.forEach(file => {
            if (file.endsWith('.jar')) {
                const filePath = path.join(modsDir, file);
                const stat = fs.statSync(filePath);

                modules.push({
                    id: `com.apexrealm:${file.replace('.jar', '').toLowerCase().replace(/[^a-z0-9]/g, '-')}:1.0.0`,
                    name: file.replace('.jar', ''),
                    type: "ForgeMod",
                    artifact: {
                        size: stat.size,
                        MD5: getMD5(filePath),
                        url: CONFIG.baseUrl + "Mod/" + encodeURIComponent(file)
                    }
                });
            }
        });
    }

    // 3. Сохраняем результат
    fs.writeFileSync('distribution.json', JSON.stringify(distro, null, 4));
    console.log('Готово! Файл distribution.json создан.');
}

generateDistro();
