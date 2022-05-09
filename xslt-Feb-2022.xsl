<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
	<xsl:output method="html" indent="yes"/>
	<xsl:template match="/WBBDLD07/IDOC">
	<xsl:variable name="alpha" select="'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'"/>
	<xsl:variable name="quote">"</xsl:variable>
	<xsl:for-each select="E1WBB01">
	<xsl:variable name="shop">http://knowrob.org/kb/shop.owl#<xsl:value-of select="MATNR_LONG"/></xsl:variable>

  LTowl:Class rdf:about="<xsl:value-of select="$shop"/>"GT





	<xsl:if test="position() != last()">		<xsl:text>,</xsl:text>		</xsl:if>
	</xsl:for-each>
</xsl:template>
</xsl:stylesheet>
