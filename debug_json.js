import fs from 'fs';
import path from 'path';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';

dotenv.config();

const root = process.env.ROOT;
console.log(`Checking files in ROOT: ${root}`);

if (!root) {
    console.error('ROOT is not defined in .env');
    process.exit(1);
}

// Check distrometa.json
const distrometaPath = path.join(root, 'meta', 'distrometa.json');
try {
    if (fs.existsSync(distrometaPath)) {
        const content = fs.readFileSync(distrometaPath, 'utf-8');
        JSON.parse(content);
        console.log(`[OK] ${distrometaPath}`);
    } else {
        console.log(`[MISSING] ${distrometaPath}`);
    }
} catch (e) {
    console.error(`[ERROR] Failed to parse ${distrometaPath}: ${e.message}`);
}

// Check servermeta.json in servers
const serversDir = path.join(root, 'servers');
if (fs.existsSync(serversDir)) {
    const servers = fs.readdirSync(serversDir);
    for (const server of servers) {
        const serverMetaPath = path.join(serversDir, server, 'servermeta.json');
        try {
            if (fs.existsSync(serverMetaPath)) {
                const content = fs.readFileSync(serverMetaPath, 'utf-8');
                JSON.parse(content);
                console.log(`[OK] ${serverMetaPath}`);
            } else {
                console.log(`[MISSING] ${serverMetaPath}`);
            }
        } catch (e) {
            console.error(`[ERROR] Failed to parse ${serverMetaPath}: ${e.message}`);
        }
    }
} else {
    console.log(`[INFO] No servers directory found at ${serversDir}`);
}
