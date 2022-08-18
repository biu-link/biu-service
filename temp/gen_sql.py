# -*- coding: utf-8 -*-

# for i in range(1, 62):
#     print(f"INSERT INTO `Tenant` (`code`, `type`, `state`, `contact`, `memo`, `name`, `shortName`, `phone`, `address`, `meta`, `descText`, `createdAt`, `updatedAt`, `deletedAt`, `version`) VALUES ('1001_{i}', '0', '', '', '', '租户_{i}', '租户_{i}', '', '', '{{}}', '', 1647434202451, 1647434202451, 0, 1);")
#

print("SELECT t.*, ta.expireAt FROM Tenant t " +
            "LEFT JOIN TenantAuthorization ta ON ta.tenantId = t.id AND ta.toTenantId = #{tenantId} AND ta.state = 'valid' AND ta.deletedAt = 0 " +
            "WHERE t.deletedAt = 0 " +
            "AND (t.id = #{tenantId} OR ta.id IS NOT NULL)")