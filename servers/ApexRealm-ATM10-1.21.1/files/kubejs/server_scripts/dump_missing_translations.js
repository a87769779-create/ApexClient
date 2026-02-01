// server_scripts/dump_missing_translations.js

console.info('[AutoTranslate] Loaded dump_missing_translations.js');

function dumpTranslations(server) {
    let targetMods = [
        'undergarden',
        'silentgear', 'silentgems',
        'pneumaticcraft',
        'productivebees', 'productivelib',
        'occultism',
        'trophymanager'
    ];

    let output = {};
    let count = 0;
    let foundItems = 0;

    console.info('[AutoTranslate] Starting dump...');

    // Get all items in the game
    let allItems = Ingredient.of('*').itemIds;
    console.info(`[AutoTranslate] Total items found in registry: ${allItems.length}`);

    // Iterate through all items
    allItems.forEach(id => {
        let parts = id.split(':');
        let namespace = parts[0];

        if (targetMods.includes(namespace)) {
            foundItems++;
            try {
                let item = Item.of(id);
                let name = id; // Fallback

                // Try different methods to get the name
                try {
                    if (item.getHoverName) {
                        name = item.getHoverName().getString();
                    } else if (item.getName) {
                        name = item.getName().getString();
                    } else if (item.hoverName) {
                        name = item.hoverName.getString();
                    } else if (item.descriptionId) {
                        name = item.descriptionId;
                    }
                } catch (err) {
                    // console.warn(`[AutoTranslate] Name retrieval failed for ${id}, using ID. Error: ${err}`);
                    // Fallback to descriptionId if possible
                    if (item.descriptionId) name = item.descriptionId;
                }

                // If name is still the ID (and simpler), try to humanize it (e.g. "my_item" -> "My Item")
                if (name === id) {
                    let parts = id.split(':')[1].split('_');
                    for (let i = 0; i < parts.length; i++) {
                        parts[i] = parts[i].charAt(0).toUpperCase() + parts[i].slice(1);
                    }
                    name = parts.join(' ');
                }

                output[id] = name;
                count++;
            } catch (e) {
                console.warn(`[AutoTranslate] Failed to process ${id}: ${e}`);
            }
        }
    });

    console.info(`[AutoTranslate] Found ${foundItems} items matching target mods.`);

    // Write to file
    JsonIO.write('kubejs/missing_translations_dump.json', output);

    let msg = `[AutoTranslate] Dumped ${count} items from target mods to kubejs/missing_translations_dump.json`;
    console.info(msg);
    if (server) {
        server.tell(Component.string(msg));
    }
    return count;
}

ServerEvents.commandRegistry(event => {
    const { commands: Commands, arguments: Arguments } = event;
    event.register(
        Commands.literal('dump_translations')
            .requires(s => s.hasPermission(2))
            .executes(c => {
                dumpTranslations(c.source.server);
                return 1;
            })
    );
});

ServerEvents.loaded(event => {
    // Run automatically on server load
    dumpTranslations(event.server);
});
