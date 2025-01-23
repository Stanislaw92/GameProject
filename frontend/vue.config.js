module.exports = {
	
	chainWebpack: (config) => {
		config.plugin('define').tap((definitions) => {
		  Object.assign(definitions[0], {
			__VUE_OPTIONS_API__: 'true',
			__VUE_PROD_DEVTOOLS__: 'false',
			__VUE_PROD_HYDRATION_MISMATCH_DETAILS__: 'false'
		  })
		  return definitions
		})
	},
	publicPath:
		process.env.NODE_ENV === 'production'
			? '/static/dist/'
			: 'http://127.0.0.1:8080',
	outputDir: '../static/dist',
	indexPath: '../../templates/index.html',
	pages: {
		index: {
			entry: 'src/main.js',
			title: 'gameProject',
		},
	},
	devServer: {
		devMiddleware: {
			publicPath: 'http://127.0.0.1:8080',
			writeToDisk: (filePath) => filePath.endsWith('index.html'),
		},
		hot: 'only',
		headers: { 'Access-Control-Allow-Origin': '*' },
	},
};
