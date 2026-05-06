import { HiringTool } from './index.js';
async function run() {
    const tool = new HiringTool('JOB-001', 'Senior Software Engineer');
    await tool.process();
}
run().catch(console.error);
//# sourceMappingURL=test.js.map