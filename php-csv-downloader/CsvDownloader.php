<?php

/**
 * 一个PHP的csv下载小工具
 */
class CsvDownloader
{
	private $delimiter;	// csv文件分隔符


	public function __construct(string $delimiter = ',')
	{
		$this->delimiter = $delimiter;
	}

	/**
	 * 设置分隔符
	 * @param string $delimiter 分隔符
	 */
	public function setDelimiter(string $delimiter = ',')
	{
		$this->delimiter = $delimiter;
	}

	/**
     * @param array $data 待下载数据
     * @param string $fileName 文件名，不用加csv
     * @param array $escapeScienceNotation  纯数字字段过长，officeExcel会自动转为科学计数法，可以通过声明这些字段避免这些字段被转换
     * @param bool $useBOM  是否添加BOM头，如不添加，officeExcel打开utf8格式的csv文件会出现中文乱码
     * @return string
     */
    public function downloadCsv(Array $data, string $fileName,Array $escapeScienceNotation = [], Array $headers = [], $useBOM = true){
        $data = array_merge([array_keys($data[0])], $data);
        $headers = array_merge($headers, ['Content-Disposition' => 'attachment; filename="'.$fileName.'.csv"',]);
        $this->_setHeaders($headers);
        $handler = fopen('php://output', 'wb+');
        if ($handler){
            if ($useBOM)
                fwrite($handler, "\xEF\xBB\xBF");
            foreach ($data as $line){
                foreach ($escapeScienceNotation as $col){
                    isset($line[$col]) && $line[$col] .= "\t";
                }
                fputcsv($handler, $line, $this->delimiter);
            }
            fclose($handler);
        }else{
            return false;
        }
    }

    /**
     * 设置并发送响应头
     * @param array $headers
     */
    protected function _setHeaders(Array $headers = [])
    {
        $default = [
            'Content-Type'        => 'application/csv; charset=UTF-8',
            'Content-Disposition' => 'attachment; filename="noName.csv"',
            'Cache-Control'       => 'no-cache',
        ];
        if (!headers_sent()){
            // 合并头信息
            $headers = array_merge($default, $headers);
            foreach ($headers as $header => $value){
                header($header . ': ' . $value);
            }
        }

    }

}